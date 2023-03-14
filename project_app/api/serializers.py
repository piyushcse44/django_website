from rest_framework.serializers import ModelSerializer
from project_app.models import project,Student

class project_serializers(ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
