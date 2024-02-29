from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone




class CustomUser(AbstractUser):
    user_type_choices=[
        ('Admin', 'Admin'),
        ('User' ,'User'),
    ]
    user_type=models.CharField(max_length=50,choices=user_type_choices,default='User')
    
    
class Admin(CustomUser):
    email_address=models.EmailField()
    

class user(CustomUser):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phone=models.CharField(max_length=100,unique=True)
    email_address=models.EmailField(unique=True)
    address=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True)
    
class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    departure_airport = models.ForeignKey(Airport, related_name='departure_airport', on_delete=models.CASCADE)
    destination_airport = models.ForeignKey(Airport, related_name='destination_airport', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()
    amount_business = models.PositiveIntegerField(default=0)
    amount_economy = models.PositiveIntegerField(default=0)
    amount_premium = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.flight_number

class Booking(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE,unique=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(default=timezone.now)
    num_seats = models.PositiveIntegerField()
    choice=[
        ('Economy', 'Economy'),
        ('Premium Economy' ,'Premium Economy'),
        ('Business', 'Business')
    ]
    seat_type=models.CharField(max_length=50,choices=choice,default='Economy')
    amount = models.PositiveIntegerField(null=True)
    choice=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    ]
    booking_status=models.CharField(max_length=100,choices=choice,default="Pending")
    


    

class Payment(models.Model):
    user= models.ForeignKey(user, on_delete=models.CASCADE,null=True)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.DateTimeField(default=timezone.now)
    choice=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    ]
    payment_status=models.CharField(max_length=50,choices=choice,default='Completed')

class Ticket(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=255)
    seat_number = models.CharField(max_length=10)

class Feedback(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


    def __str__(self):
        return f"Feedback from {self.user.username}"

class Promotion(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_amount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateField()
    valid_to = models.DateField()

class FlightSchedule(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    departure_day = models.CharField(max_length=20)  
    departure_time = models.TimeField()
    arrival_day = models.CharField(max_length=20)  
    arrival_time = models.TimeField()

class Aircraft(models.Model):
    aircraft_type = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, unique=True)
    seating_capacity = models.PositiveIntegerField()