from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from adminapi import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("users",views.UserView,basename="users")
router.register("airports",views.AirportView,basename="airports")
router.register("paymentstatus",views.PaymentView,basename="paymentstatus")
router.register("feedbacks",views.FeedbackView,basename="feedbacks")
router.register("flights",views.FlightView,basename="flights")



urlpatterns = [
    path("register/",views.AdminCreateView.as_view(),name="signup"),
    path("token/",ObtainAuthToken.as_view(),name="token"),
    path("profile/",views.ProfileEdit.as_view(),name="profile"),
] +router.urls
