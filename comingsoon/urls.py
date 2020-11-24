from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'comingsoon'

urlpatterns = [
    path('', views.home, name='home'),
    path('comingsoon/milk.html/', views.milk, name='milk'),
    path('comingsoon/eggs.html/', views.eggs, name='eggs'),
    path('comingsoon/bread.html/', views.bread, name='bread'),
    path('comingsoon/yoghurt.html/', views.yoghurt, name='yoghurt'),
    path('comingsoon/potatoes.html/', views.potatoes, name='potatoes'),
    path('comingsoon/milk_groupshop.html/', views.milk_gp, name='milk-groupshop'),
    path('comingsoon/yoghurt_groupshop.html/', views.yoghurt_gp, name='milk-yoghurt'),
    path('comingsoon/bread_groupshop.html/', views.bread_gp, name='bread-yoghurt'),
    path('comingsoon/eggs_groupshop.html/', views.eggs_gp, name='eggs-yoghurt'),
    path('comingsoon/delivery_milk.html/', views.delivery_milk, name='delivery_milk'),
    path('comingsoon/delivery_yoghurt.html/', views.delivery_yoghurt, name='delivery_yoghurt'),
    path('comingsoon/delivery_eggs.html/', views.delivery_eggs, name='delivery_eggs'),
    path('comingsoon/delivery_bread.html/', views.delivery_bread, name='delivery_bread'),
    path('comingsoon/milk_alone.html/', views.milk_alone, name='milk_alone'),
    path('comingsoon/yoghurt_alone.html/', views.yoghurt_alone, name='yoghurt_alone'),
    path('comingsoon/eggs_alone.html/', views.eggs_alone, name='eggs_alone'),
    path('comingsoon/bread_alone.html/', views.bread_alone, name='bread_alone'),
    
] 

