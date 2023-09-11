from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("viewList/", views.viewList, name="viewList"),
    path("delete_purchase/<or_numbers>", views.delete_purchase, name="delete_purchase"),
    path("update_purchase/<or_numbers>", views.update_purchase, name="update_purchase"),
]