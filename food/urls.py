from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexClassView.as_view() , name="index"),
    path('food/', views.food , name="food"),
    path('<int:pk>/', views.DetailViewItem.as_view(), name='details'),
    path('add/', views.CreateItem.as_view(), name='create_form'),
    path('update/<int:id>/', views.update , name='update'),
    path('delete/<int:id>/', views.delete_item , name='delete_item')
]