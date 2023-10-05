from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Client, Order, Product

def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)
    today = datetime.now()
    last_7_days = today - timedelta(days=7)
    last_30_days = today - timedelta(days=30)
    last_365_days = today - timedelta(days=365)

    last_7_days_orders = Order.objects.filter(client=client, order_date__gte=last_7_days)
    last_30_days_orders = Order.objects.filter(client=client, order_date__gte=last_30_days)
    last_365_days_orders = Order.objects.filter(client=client, order_date__gte=last_365_days)

   
    last_7_days_products = set(product for order in last_7_days_orders for product in order.products.all())
    last_30_days_products = set(product for order in last_30_days_orders for product in order.products.all())
    last_365_days_products = set(product for order in last_365_days_orders for product in order.products.all())

    return render(request, 'myapp/client_orders.html', {
        'last_7_days': last_7_days_products,
        'last_30_days': last_30_days_products,
        'last_365_days': last_365_days_products,
    })
