from rest_framework import serializers
from adminapi.models import Admin,user,Airport,Aircraft,Payment,Feedback,Flight



class AdminSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=Admin
        fields=["id","username","email_address","password"]

    def create(self, validated_data):
        return Admin.objects.create_user(**validated_data)
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=["id","firstname","lastname","phone","email_address","is_available","date_joined"]
        
        
class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Airport
        fields="__all__"
        
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields="__all__"
        

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields="__all__"
        

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields="__all__"