from django.urls import path
from . import views
from .views import home, landing ,calorie_cal, calorie_counter, ovulation , menstruation, delete_fooditem

urlpatterns = [

    path('',views.landing,name='landing-page'),
    path('home/',views.home,name='home'),
    path('calorie-cal/',views.calorie_cal,name='calorie_cal'),
    path('calorie-counter/',views.calorie_counter,name='calorie_counter'),
    path('delete_fooditem/<int:id>/',views.delete_fooditem,name='delete_fooditem'),
    path('ovulation/',views.ovulation,name='ovulation'),
    path('menstruation/',views.menstruation,name='menstruation'),
]