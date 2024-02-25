from django.urls import path
from userapi import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("flights",views.FlightView,basename="flights")
router.register("userflightlist",views.UserFlights,basename="userflightlist"),

urlpatterns = [
    path("register/",views.UserCreateView.as_view(),name="signup"),
    path("token/",ObtainAuthToken.as_view(),name="token"),  
    path("profile/",views.ProfileEdit.as_view(),name="profile"),
    
 
] +router.urls
