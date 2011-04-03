from django.db import models
# Using Django User as the basic User Profile
from django.contrib.auth.models import User,UserManager

# Create your models here.

class Buyer(User):
    """
    Adding any field to hold Buyer personal info
    """
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()



class Background(models.Model):
    """
    This model holds basic background which are 
    exposable.
    Make it abstract. To the end, will implement in porfile class
    """
    EDUCATION_CHOICE = (
        ('Undergraduate','Undergraduate'),
        ('Graduate','Graduate'),
    )
    
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICE)
    
    OCCUPTION_CHOICE = (
        ('Student','Student'),
        ('Officer','Officer'),
    )
    
    occuption = models.CharField(max_length=20, choices=OCCUPTION_CHOICE)
    
    class Meta:
        abstract = True

class FamilyBackground (Background):
    MARRIAGE_CHOICE = (
        ('Married','Married'),
        ('Single','Single'),
    )

    marriage = models.CharField(max_length=10, choices=MARRIAGE_CHOICE)
    family_size = models.IntegerField()
    number_of_kids = models.IntegerField()

    TYPE_CHOICE = (
        ('Extended','Extended'),
        ('Joint','Joint'),
        ('Unclear','Unclear'),
    )

    famile_type = models.CharField(max_length=10, choices=TYPE_CHOICE)

    class Meta:
        abstract = True

class PersonalChar (FamilyBackground):
    PERSONAL_CHAR_CHOICE = (
        ('Smoking','Smoking'),
        ('Alcohol','Alcohol'),
        ('Parties','Parties'),
    )

    person_char = models.CharField(max_length=20 , choices=PERSONAL_CHAR_CHOICE)

    RELIGION_CHOICE = (
        ('Christianity','Christianity'),
        ('Islam','Islam'),
        ('Buddhism','Buddhism'),
        ('Hinduism','Hinduism'),
    )

    religion = models.CharField(max_length=30 , choices=RELIGION_CHOICE)

    class Meta:
        abstract = True


class PropertyProfile(models.Model):
    TYPE_OF_HOUSE_CHOICE = (
        ('Independent','Independent'),
        ('Flat','Flat'),
        ('Condo','Condo'),
    )

    type_house = models.CharField(max_length=20 , choices=TYPE_OF_HOUSE_CHOICE)

    NUMBER_OF_ROOM = (
        ('1BR','1 Bedroom'),
        ('2BR','2 Bedroom'),
    )

    number_room = models.CharField(max_length=20 , choices=NUMBER_OF_ROOM)
    square_feet = models.IntegerField()
    loc = models.CharField(max_length=40)

    RENT_SELL_CHOICE = (
        ('Rent','Rent'),
        ('Sell','Sell'),
    )

    rent_or_sell = models.CharField(max_length=15, choices=RENT_SELL_CHOICE)
    price = models.IntegerField()
    loc = models.CharField(max_length=50)

    class Meta:
        abstract = True

class BuyerProfile(PersonalChar):
    buyer = models.ForeignKey(Buyer)
    
    NOTIFY_CHOICE = (
        ('SMS','Text Message'),
        ('EMAIL','EMail'),
    )
    notify = models.CharField(max_length=10, choices=NOTIFY_CHOICE)

class BuyerInterestProperty(PropertyProfile):
    buyer = models.ForeignKey(Buyer)

class Seller(User):
    TYPE_OF_SELLER = (
        ('Landlord','Landlord'),
        ('Agency','Agency'),
        ('Builder','Builder'),
        ('Broker','Broker'),
    )
    type_seller = models.CharField(max_length=10, choices=TYPE_OF_SELLER)
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()

class HouseProfile(PropertyProfile):
    seller = models.ForeignKey(Seller)
