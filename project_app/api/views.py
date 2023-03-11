from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_app.models import project
from project_app.api.serializers import project_serializers

@api_view(['GET','PUT','DELETE','POST'])
def Json_formate(request):
    list =[
        'piyush',
        'ayush',
        'prince',
        'parash',
        'ojha',
        'jyoti'
    ]
    return Response(list)

@api_view(['GET','DELETE'])
def json_project(request):
    projects = project.objects.all()
    serializers = project_serializers(projects,many=True)
    return(Response(serializers.data))
