from django.urls import path
from .import views

urlpatterns = [

    path('', views.login, name='login'),
    path('logincheck/', views.logincheck, name='verify_login'),
    path('home/', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('deleteuser/<int:id>', views.deleteme, name='delete'),
    path('edituser/<int:id>', views.editme, name='edit'),
    path('searchdata/', views.searchdata, name='search'),
    path('logout/', views.logout, name='logout'),

]
