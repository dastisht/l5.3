from django.urls import path
from . import views

urlpatterns = [
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),
]
