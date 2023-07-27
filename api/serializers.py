from rest_framework import serializers
from api.models import Student

class StudenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id","name","roll","city"]