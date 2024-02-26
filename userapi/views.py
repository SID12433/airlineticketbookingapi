from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status

from userapi.serializer import UserSerializer,FlightSerializer,BookingSerializer,PaymentSerializer,FeedbackSerializer
from adminapi.models import user,Flight,Payment,Feedback,Booking,Airport



class UserCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_type="User")
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ProfileEdit(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def get(self,request,*args,**kwargs):
        user_id=request.user.id
        qs=user.objects.get(id=user_id)
        serializer=UserSerializer(qs)
        return Response(data=serializer.data)
    
    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class FlightView(ViewSet):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    
    
    def list(self,request,*args,**kwargs):
        qs=Flight.objects.all()
        serializer=FlightSerializer(qs,many=True)
        for data in serializer.data:
            departure_airport_id = data.pop('departure_airport')
            destination_airport_id = data.pop('destination_airport')
            departure_airport_code = Airport.objects.get(pk=departure_airport_id).code  
            destination_airport_code = Airport.objects.get(pk=destination_airport_id).code
            data['departure_airport'] = departure_airport_code
            data['destination_airport'] = destination_airport_code

        return Response(serializer.data)
    

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Flight.objects.get(id=id)
        serializer=FlightSerializer(qs)
        return Response(data=serializer.data)
    
    @action(methods=["post"],detail=True)
    def booking_seat(self,request,*args,**kwargs):
        serializer=BookingSerializer(data=request.data)
        flight_id=kwargs.get("pk")
        user_id=request.user.id
        user_obj=user.objects.get(id=user_id)
        flight_obj=Flight.objects.get(id=flight_id)
        
        if serializer.is_valid():
            seat_type = serializer.validated_data.get('seat_type')
            num_seats = serializer.validated_data.get('num_seats')
            amount = self.calculate_amount(flight_obj, seat_type, num_seats)
            serializer.save(flight=flight_obj, user=user_obj, amount=amount)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def calculate_amount(self, flight, seat_type, num_seats):
        if seat_type == 'Economy':
            return flight.amount_economy * num_seats
        elif seat_type == 'Premium Economy':
            return flight.amount_premium * num_seats
        elif seat_type == 'Business':
            return flight.amount_business * num_seats
        else:
            return 0
        
        
    @action(methods=["post"],detail=True)
    def feedback(self,request,*args,**kwargs):
        serializer=FeedbackSerializer(data=request.data)
        flight_id=kwargs.get("pk")
        flight_obj=Flight.objects.get(id=flight_id)
        user_id=request.user.id
        user_obj=user.objects.get(id=user_id)
        if serializer.is_valid():
            serializer.save(flight=flight_obj,user=user_obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    
class UserFlights(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        user_id=request.user.id
        user_obj=user.objects.get(id=user_id)
        qs=Booking.objects.get(user=user_obj)
        serializer=BookingSerializer(qs)
        return Response(data=serializer.data)
    
    @action(methods=["post"],detail=True)
    def payment(self,request,*args,**kwargs):
        serializer=PaymentSerializer(data=request.data)
        booking_id=kwargs.get("pk")
        booking_obj=Booking.objects.get(id=booking_id)
        user_id=request.user.id
        user_obj=user.objects.get(id=user_id)
        if serializer.is_valid():
            serializer.save(booking=booking_obj,user=user_obj,amount=booking_obj.amount)
            booking_obj.booking_status="Completed"
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    
    