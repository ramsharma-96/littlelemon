from django.contrib import admin 
from django.urls import include, path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'table', views.BookingViewSet)

  
urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', include(router.urls)),

]