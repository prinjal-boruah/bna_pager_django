from rest_framework import serializers 
from .models import *
 
 
class SpeechSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = SpeechData
        fields = ['text','lang',]