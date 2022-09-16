from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_index, name="product.index"),
    path("products/create/", views.product_create, name="product.create"),
    path("products/show/<int:id>/", views.product_show, name="product.show"),
    path("products/edit/<int:id>/", views.product_edit, name="product.edit"),
    path("products/update/", views.product_update, name="product.update"),
    path("products/delete/<int:id>/", views.product_delete, name="product.delete"),
]