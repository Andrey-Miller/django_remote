from datetime import timedelta
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404

from .forms import OrderForm
from .models import User, Order


def fetch_order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def fetch_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})


def fetch_user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(user=user)
    context = {
        'user': user,
        'orders': orders,
    }
    return render(request, 'orders/orders.html', context)



def fetch_ordered_products_by_days(request, user_id, num_days):
    user = get_object_or_404(User, pk=user_id)
    today = timezone.now().date()
    start_date = today - timedelta(days=num_days)
    orders = Order.objects.filter(user=user, order_date__gte=start_date)

    products = set()

    for order in orders:
        products.update(order.products.all())

    context = {
        'user': user,
        'products': products,
        'num_days': num_days,
    }
    return render(request, 'orders/ordered_products_sort.html', context)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            form.save_m2m()
            return redirect('add_user_products', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

def add_user_products(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save(commit=False)
            form.save_m2m()
            form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/add_user_products.html', {'form': form, 'order': order})