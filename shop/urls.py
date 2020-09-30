from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('product-list/', views.product_list, name='product_list'),
    path('<str:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<str:id>/<str:slug>/', views.product_detail, name='product_detail'),
]