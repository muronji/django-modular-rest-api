# services.py
import requests
from decimal import Decimal
from .models import Order
from customers.models import Customer

FAKESTORE_ORDERS_URL = "https://fakestoreapi.com/carts"
FAKESTORE_USER_URL = "https://fakestoreapi.com/users/{}"

def fetch_and_save_external_orders():
    response = requests.get(FAKESTORE_ORDERS_URL)
    if response.status_code != 200:
        return [], "Failed to fetch orders"

    orders_data = response.json()
    saved_orders = []

    for external_order in orders_data:
        user_id = external_order['userId']
        # Fetch or create customer
        res = requests.get(FAKESTORE_USER_URL.format(user_id))
        if res.status_code != 200:
            continue
        user_data = res.json()
        email = user_data.get("email")
        customer, created = Customer.objects.get_or_create(
            email=email,
            defaults={
                "first_name": user_data['name']['firstname'],
                "last_name": user_data['name']['lastname'],
                "phone_number": user_data.get('phone', '')
            }
        )

        # Calculate total amount
        total_amount = Decimal(sum([p['quantity'] * 10 for p in external_order['products']]))  # fake price

        order = Order.objects.create(
            customer=customer,
            total_amount=total_amount,
            status=False
        )
        saved_orders.append(order)

    return saved_orders, None
