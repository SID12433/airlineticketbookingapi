from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import status
from rest_framework.decorators import action

from adminapi.serializer import AdminSerializer,UserSerializer,AirportSerializer,PaymentSerializer,FeedbackSerializer,FlightSerializer
from adminapi.models import Admin,user,Flight,Aircraft,Airport,Payment,Feedback


class AdminCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_type="Admin",is_superuser=True)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
        
class ProfileEdit(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def get(self,request,*args,**kwargs):
        admin=request.user.id
        qs=Admin.objects.get(id=admin)
        serializer=AdminSerializer(qs)
        return Response(data=serializer.data)
    
    def put(self, request, *args, **kwargs):
        admin = request.user
        serializer = AdminSerializer(admin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=user.objects.all()
        serializer=UserSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=user.objects.get(id=id)
        serializer=UserSerializer(qs)
        return Response(data=serializer.data)
    

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            instance = user.objects.get(id=id)
            instance.delete()
            return Response({"msg": "User removed"})
        except user.DoesNotExist:
            return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

class AirportView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self,request,*args,**kwargs):
        serializer=AirportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def list(self,request,*args,**kwargs):
        qs=Airport.objects.all()
        serializer=AirportSerializer(qs,many=True)
        data=serializer.data
        airport_count=Airport.objects.count()
        data_with_count={'airport_count': airport_count, 'airports': data}
        return Response(data=data_with_count)
    
    def update(self,request,*args,**kwargs): 
        id=kwargs.get("pk")
        obj=Airport.objects.get(id=id)
        serializer=AirportSerializer(data=request.data,instance=obj)
        if request.user.admin:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        else:
            return Response(data={"message":"permission denied"})
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Airport.objects.get(id=id)
        serializer=AirportSerializer(qs)
        return Response(data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            instance = Airport.objects.get(id=id)
            instance.delete()
            return Response({"msg": "Airport removed"})
        except Airport.DoesNotExist:
            return Response({"msg": "Airport not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        
class PaymentView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=Payment.objects.all()
        serializer=PaymentSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Payment.objects.get(id=id)
        serializer=PaymentSerializer(qs)
        return Response(data=serializer.data)
    

class FeedbackView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=Feedback.objects.all()
        serializer=FeedbackSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Feedback.objects.get(id=id)
        serializer=FeedbackSerializer(qs)
        return Response(data=serializer.data)
    
    

class FlightView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self,request,*args,**kwargs):
        serializer=FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def list(self,request,*args,**kwargs):
        qs=Flight.objects.all()
        serializer=FlightSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def update(self,request,*args,**kwargs): 
        id=kwargs.get("pk")
        obj=Flight.objects.get(id=id)
        serializer=FlightSerializer(data=request.data,instance=obj)
        if request.user.admin:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        else:
            return Response(data={"message":"permission denied"})
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Flight.objects.get(id=id)
        serializer=FlightSerializer(qs)
        return Response(data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            instance = Flight.objects.get(id=id)
            instance.delete()
            return Response({"msg": "Flight removed"})
        except Flight.DoesNotExist:
            return Response({"msg": "Flight not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
