from django.db import models

from users.models import User
from services.models import ServicesModel, ServiceTierModel

# TODO: add gettext_lazy

class PaymentModel(models.Model):
    """Contains information on customer transactions
    """
    # foreign keys
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    service = models.ForeignKey(ServiceTierModel, on_delete=models.PROTECT)
    
    # transaction information
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    currency = models.CharField(max_length=3, default="USD", blank=False, null=False)
    payment_intent_id = models.CharField(max_length=100, blank=False, null=False)
    payment_method_id = models.CharField(max_length=100, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False, null=False)
