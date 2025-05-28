from rest_framework import serializers
from .models import borrow_logs

class borrow_logsSerializer(serializers.ModelSerializer):
    class Meta:
        model = borrow_logs
        fields = '__all__'