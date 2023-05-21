from rest_framework import serializers
from services.models import User

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]