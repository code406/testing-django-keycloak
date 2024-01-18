from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_world, name="hello_world"),
    path("register_user/", views.register_user, name="register_user"),
    path("set_user_field/", views.set_user_field, name="set_user_field"),
]
