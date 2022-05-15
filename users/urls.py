from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import SignUpView, UserLoginView, UserListView, list_of_users
from django.contrib.auth.models import Permission
urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list/', UserListView.as_view(), name='list'),
    path('lista-lukasza/', list_of_users, name='lista_lukasza'),

]
