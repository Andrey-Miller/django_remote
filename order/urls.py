from django.urls import path

from .views import fetch_user_orders, fetch_ordered_products_by_days
from .views import fetch_order_list, fetch_order, create_order, add_user_products

urlpatterns = [
    path('user-orders/<int:user_id>', fetch_user_orders, name='user_orders'),
    path('ordered-products-by-days/<int:user_id>/<int:num_days>', fetch_ordered_products_by_days,
         name='ordered_products_by_days'),
    path('list/', fetch_order_list, name='order_list'),
    path('<int:order_id>/', fetch_order, name='order_detail'),
    path('create/', create_order, name='create_order'),
    path('<int:order_id>/add/', add_user_products, name='add_user_products'),
]
