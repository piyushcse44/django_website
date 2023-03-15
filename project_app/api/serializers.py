from rest_framework import serializers
from project_app.models import project,Student

class project_serializers(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
