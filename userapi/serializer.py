from rest_framework import serializers
from adminapi.models import user,Flight,Booking,Payment,Feedback


class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    is_available=serializers.CharField(read_only=True)

    class Meta:
        model=user
        fields=["id","username","firstname","lastname","phone","email_address","password","is_available"]

    def create(self, validated_data):
        return user.objects.create_user(**validated_data)
    
    
    
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields="__all__"
        
        
class BookingSerializer(serializers.ModelSerializer):
    flight=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Booking
        fields="__all__"
        

class PaymentSerializer(serializers.ModelSerializer):
    amount=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    booking=serializers.CharField(read_only=True)
    class Meta:
        model=Payment
        fields="__all__"
        
        
class FeedbackSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Feedback
        fields="__all__"