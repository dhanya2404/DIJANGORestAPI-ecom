from rest_framework import serializers
from .models import doto

class dotoserializers(serializers.ModelSerializer):
    class Meta:
        model = doto
        fields = '__all__' 