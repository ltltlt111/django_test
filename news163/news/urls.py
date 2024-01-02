from django.urls import path
from . import  views



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('detail/<new_id>', views.detail, name='detail'),
    path('category/<category_id>', views.category, name='category'),
]