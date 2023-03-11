from rest_framework.serializers import ModelSerializer
from project_app.models import project

class project_serializers(ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'

