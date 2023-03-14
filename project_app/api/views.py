from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_app.models import project,Student
from project_app.api.serializers import project_serializers,StudentSerializer
import io
from django.http import HttpResponse

api_url =[
        '/api/',
        '/api/student/',
        '/api/student/id/'
    ]


@api_view(['GET','PUT','DELETE','POST'])
def Json_formate(request):
    return Response(api_url)


@api_view(['GET','DELETE'])
def json_project(request):
    projects = project.objects.all()
    serializers = project_serializers(projects,many=True)
    return(Response(serializers.data))


@api_view(['GET','POST'])
def StudentApiWithoutId(request):
    if(request.method == 'POST'):
        json_input = request.body
        stream = io.BytesIO(json_input)
        
        return Response(api_url)
    else:
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset,many = True)
        return Response(serializer.data)
     
@api_view(['DELETE','PUT','GET'])
def StudentApiWithId(request,pk):  
    try:
        queryobject = Student.objects.get(id = pk)
        id = queryobject.id
        if id == None:
            return Response({"invalid : INVALID"})
 
        elif request.method == 'DELETE':
            queryobject.delete()
        else:
            serializer = StudentSerializer(queryobject,many = False)
            return Response(serializer.data)  
    except :
        return Response({"invalid : INVALID"})


        
