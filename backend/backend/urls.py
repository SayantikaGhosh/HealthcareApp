"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from user import views as user_view
from base import views as base_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='register'),
    path('calorie-cal/', base_view.calorie_cal, name = 'calorie-cal'),
    path('calorie-counter/',base_view.calorie_counter,name='calorie_counter'),
    path('delete_fooditem/<int:id>/', base_view.delete_fooditem, name = 'delete_fooditem'),
    path('ovulation/', base_view.ovulation, name = 'ovulation'),
    path('menstruation/', base_view.menstruation, name = 'menstruation'),
    path('recommend-yoga/', base_view.recommend, name = 'recommend-yoga'),
    # path('login/', user_view.login_page, name='login'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
     path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('', include('base.urls')),
    
]

