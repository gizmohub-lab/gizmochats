
from django.urls import path,include
from . import views
urlpatterns = [
    path('home/<str:username>/',views.home,name='home'),
    path('',views.loggin,name='login'),
    path('logout/',views.loggout,name='logout')
    
   
]
