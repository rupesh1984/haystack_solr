from django.urls import path
from .views import UserView

urlpatterns = [
    path('list', UserView.list_users, name='list-users'),
    path('create', UserView.create_user, name='create-user'),
]