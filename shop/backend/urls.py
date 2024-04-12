
from django.contrib import admin
from django.urls import path, include
from backend import views
from backend.views import AllProductsView, ProductView, CategoryView, ContactTemplateView

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),

    path('register/', views.register, name='register'),

    path('', views.HomeTemplateView.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductTemplateView.as_view(), name='product'),
    path('category/<int:pk>/', views.CategoryTemplateView.as_view(), name='category'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('products/', AllProductsView.as_view(), name='products'),
    path('products/<int:product_id>/', ProductView.as_view(), name='product_detailed'),
    path('products/category/<int:category_id>/', CategoryView.as_view(), name='category_id'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),

]
