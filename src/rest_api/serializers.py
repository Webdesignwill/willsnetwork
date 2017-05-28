from rest_framework import serializers

from contacts import models


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contact
        fields = ('email', 'created', 'created_ip_address', 'message')
