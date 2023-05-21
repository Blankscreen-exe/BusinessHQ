from django.db import models

from django.contrib.auth.models import AbstractUser

# TODO: use translator gettext_lazy

# TODO: add user types and roles
class UserType(models.IntegerChoices):
    ADMIN = 0, 'Admin'
    RESOURCE_MANAGER = 1, 'Resource Manager'
    CUSTOMER_HANDLER = 2, 'Customer Handler'
    CUSTOMER = 3, 'Customer'
    
class User(AbstractUser):
    """Model for all users in our app. Contains all basic details.
    """
    # auth fields
    username = models.CharField(unique=True ,max_length=125, blank=False, null=False, default=None)
    email = models.CharField(unique=True, max_length=255, blank=False, null=False)
    password = models.CharField(unique=True, max_length=255, blank=False, null=False)
    
    # access privilege fields
    # role = models.PositiveSmallIntegerField(choices=UserType.choices, default=UserType.CUSTOMER)
    
    @property
    def role(self):
        # Compute role based on usergroup
        if self.usergroup == self.ADMIN:
            return self.ADMIN
        elif self.usergroup == self.MANAGER:
            return self.MANAGER
        elif self.usergroup == self.HANDLER:
            return self.HANDLER
        else:
            return self.CUSTOMER
    
    # payment gateway id (stripe)
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    
    # general information
    # TODO: add more information. this will go in user profiles
    first_name = models.CharField(max_length=125, blank=True, null=True)
    last_name = models.CharField(max_length=125, blank=True, null=True)
    
    # TODO: add fields related to user status(boolean) such as address_submitted
    
    # TODO: make it accept emails instead of username during login
    # setting default login username field --> email
    # USERNAME_FIELD = 'email'
    # required "additional" fields during sign-up(apart from "auth fields": look at the first 3 fields of this model)
    # REQUIRED_FIELDS = []

class UserGroup(models.Model):
    ADMIN = 0
    MANAGER = 1
    HANDLER = 2
    CUSTOMER = 3

    GROUP_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Resource Manager'),
        (HANDLER, 'Customer Handler'),
        (CUSTOMER, 'Customer'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, default=CUSTOMER)

class UserAddressModel(models.Model):
    """Contains information on user's address. Mainly for 'Customer' user types 
    """
    # foreign keys
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # address infromation
    country = models.CharField(max_length=125, blank=True, null=True)
    city = models.CharField(max_length=125, blank=True, null=True)
    zip_code = models.CharField(max_length=125, blank=True, null=True)
    time_zone = models.CharField(max_length=125, blank=True, null=True)
    
class UserCardModel(models.Model):
    """Contains payment and card details as provided by payment gateway
    """
    # foreign keys
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # payment details
    payment_card_id = models.CharField(max_length=225, blank=True, null=True)
