from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User

# TODO: add gettext_lazy

class ChatSessionModel(models.Model):
    """Contains session details between customer and their handlers
    """
    # foreign key
    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='customer_sessions')
    handler = models.ForeignKey(User, on_delete=models.PROTECT, related_name='handler_sessions')

    # session details
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField()
    
    def __str__(self):
        return f"Chat session between {self.customer.username} and {self.handler.username}"

class MessageModel(models.Model):
    """Contains all messages in a chat session in ChatSessionModel
    """
    # foreign key
    session = models.ForeignKey(ChatSessionModel, on_delete=models.PROTECT)
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # message details
    content = models.TextField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}-{self.content}"
    
class ChatSessionReviewModel(models.Model):
    """Contains review information for each chat session in ChatSessionModel
    """
    # foreign key
    session = models.ForeignKey(ChatSessionModel, on_delete=models.PROTECT)
    
    # message details
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
        return f"{self.session.id}-{self.rating}"
