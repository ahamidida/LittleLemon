from django.urls import path
from . import views
urlpatterns = [
    path('', views.MenuItemView.as_view()),
    path('<int:pk>/', views.SingleMenuItemView.as_view()),
]