from django.urls import path

from .views import add_user, fetch_user, fetch_user_list, edit_user

urlpatterns = [
    path('list/', fetch_user_list, name='user_list'),
    path('<int:user_id>/', fetch_user, name='user_view'),
    path('add/', add_user, name='add_user'),
]