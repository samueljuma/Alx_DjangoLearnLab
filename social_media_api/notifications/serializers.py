from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source="actor.username", read_only=True)
    
    class Meta:
      model = Notification
      fields = ["id", "recipient", "actor", "actor_username", "verb", "content_type", "object_id", "timestamp"]
      read_only_fields = ["id", "recipient", "actor", "verb", "content_type", "object_id", "timestamp"]
