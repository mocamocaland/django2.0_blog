from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /blog/
    path('add/', views.AddView.as_view(), name='add'), # /blog/add
    path('update/<int:pk>/', views.update, name='update'), #/blog/update/1 <int:pk>整数ならなんでも受け取る
    path('delete/<int:pk>/', views.delete, name='delete'), #/blog/delete/1
    path('detail/<int:pk>/', views.detail, name='detail'), #/blog/detail/1/
]
