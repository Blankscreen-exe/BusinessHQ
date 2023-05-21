from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

from users.models import User

# TODO: add gettext_lazy

class ServiceTagModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=125, blank=False, null=False, default="N/A")

    def __str__(self):
        return self.name
    
class ServicesModel(models.Model):
    """Model for storing all service details within the platform
    """
    tags = models.ManyToManyField('ServiceTagModel', blank=True)
    
    title = models.CharField(max_length=125, blank=False, null=False, default="N/A")
    date_created = models.DateTimeField(default=timezone.now, blank=False, null=False)   

    def __str__(self):
        return self.title 

class ServiceTierModel(models.Model):
    """Contains Tier information for each Service in ServiceModel
    """
    # foreign keys
    service = models.ForeignKey(ServicesModel, on_delete=models.PROTECT)
    
    # tier details
    tier = models.IntegerField(blank=False, null=False, default=0)
    sub_title = models.CharField(max_length=125, blank=False, null=False, default="N/A")
    description = models.TextField(max_length=225, blank=False, null=False, default="N/A")
    average_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.service.title}-{self.tier}"

class ServiceReviewsModel(models.Model):
    """Contains review information for each service in the ServiceModel
    """
    # foriegn keys
    service = models.ForeignKey(ServicesModel, on_delete=models.PROTECT)
    reviewed_by = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # review information
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    
    def __str__(self):
        return f"{self.service.title}-{self.reviewed_by.first_name} {self.reviewed_by.last_name}"
    
class ServicesOngoingModel(models.Model):
    """Contains information on any services that are ongoing for a certain client
    """
    # foreign keys
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    service = models.ForeignKey(ServiceTierModel, on_delete=models.PROTECT)
    
    # service status
    STATUS_CHOICES = (
        (0, 'Initial Meetup'),
        (1, 'Working'),
        (2, 'Waiting For Review'),
        (3, 'Meeting'),
        (4, 'Change Requirements'),
        (5, 'Finalizing'),
        (6, 'Presenting'),
        (7, 'Finished'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, blank=False, null=False, default=0)
    
    # booked service details
    date_booked = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    date_first_meetup = models.DateTimeField(default=timezone.now, blank=False, null=False)
    date_last_meetup = models.DateTimeField(default=timezone.now, blank=False, null=False)
    milestones = models.IntegerField(blank=False, null=False, default=1)
    total_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    time_spent = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    time_est = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f"{self.customer} ordered service {self.service.service.title}"