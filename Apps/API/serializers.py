from rest_framework import serializers
from .models import DATA



class DataSer(serializers.ModelSerializer):
    class Meta:
        model = DATA
        fields = ['id', 'name', 'des']

