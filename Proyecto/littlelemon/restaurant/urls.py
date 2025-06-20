#define URL route for index() view
from django.urls import path
from .views import MenuItemView, SingleMenuItemView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

#add following lines to urlpatterns list 
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items', views.MenuItemView.as_view(), name ='menu-items'),
    path('menu/items<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token),
]

