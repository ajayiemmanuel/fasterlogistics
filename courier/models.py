from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    address = models.CharField (max_length = 200,  null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    city = models.CharField (max_length = 200, null = True)


    def __str__(self):
        return self.address



class Product (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    order = models.CharField (max_length = 200, null = True)
    expected_arrival = models.CharField (max_length = 200,  null = True)
    usps = models.CharField (max_length = 200, null = True)
    destination = models.CharField (max_length = 200, null = True)
    delivery = models.CharField (max_length = 200, null = True)
    package_name = models.CharField (max_length = 200, null = True)
    order_date = models.CharField (max_length = 200, null = True)
    delivery_date = models.CharField (max_length = 200, null = True)
    reciever_name = models.CharField (max_length = 200, null = True)    
    status = models.CharField (max_length = 200, null = True)
    address = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    postal_code = models.CharField (max_length = 200, null = True)
    profile_pic = models.ImageField (default = "ship.jpg", null = True, blank = True)
    origin = models.CharField (max_length = 200, null = True)
    shipping_amount = models.CharField (max_length = 200, null = True)


    def __str__(self):
        return self.order        



class Tracking (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    first_step = models.CharField (max_length = 200, null = True)
    second_step = models.CharField (max_length = 200,  null = True)
    third_step = models.CharField (max_length = 200, null = True)
    fourth_step = models.CharField (max_length = 200, null = True)
    fifth_step = models.CharField (max_length = 200, null = True)
    sixth_step = models.CharField (max_length = 200, null = True)


    def __str__(self):
        return self.first_step      


class Step4 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    info = models.CharField (max_length = 200, null = True)
    location = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)

    def __str__(self):
        return self.info     


class Step5 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    info = models.CharField (max_length = 200, null = True)
    location = models.CharField (max_length = 200,  null = True)
    date = models.CharField (max_length = 200, null = True)

    def __str__(self):
        return self.info  

class Step6 (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    arrived = models.CharField (max_length = 200, null = True)

    def __str__(self):
        return self.arrived  