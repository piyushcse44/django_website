from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_app.models import project,Student
from project_app.api.serializers import project_serializers,StudentSerializer
import io
from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import json


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


@api_view(['GET','POST','PUT'])
def StudentApiWithoutId(request):


    if(request.method == 'POST'):
        json_input = request.body
        stream = io.BytesIO(json_input)
        parsed_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=parsed_data)
        if(serializer.is_valid()):
            serializer.save()
            return Response("succesfully saved")
        else:
            return Response(serializer.errors)   


    if request.method == 'PUT':
        json_input = request.body
        stream = io.BytesIO(json_input)
        parsed_data = JSONParser().parse(stream)     
        try:
            id = parsed_data.get('id')
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu,data = parsed_data,partial = True)
           
            if serializer.is_valid():
                serializer.save()
                return Response("Updated Successfull")
            else:
                return Response(serializer.errors)    
           
        except:
            return Response("No Id present")


    queryset = Student.objects.all()
    serializer = StudentSerializer(queryset,many = True)
    return Response(serializer.data)
     

    
@api_view(['DELETE','PUT','GET'])
def StudentApiWithId(request,pk):  
    try:
        queryobject = Student.objects.get(id = pk)
        id = queryobject.id

        if id == None:
            return Response("INVALID KEY")
 
        if request.method == 'DELETE':
            queryobject.delete()
            return Response("Successfully Deleted")

        if request.method == 'GET':
            serializer = StudentSerializer(queryobject,many = False)
            return Response(serializer.data)  
        
        if request.method == 'PUT':
            json_input = request.body
            stream = io.BytesIO(json_input)
            parsed_data = JSONParser().parse(stream)
            deserilize = StudentSerializer(queryobject, data=parsed_data)    
            if(deserilize.is_valid()):               
                deserilize.save()
                return Response("Successfully updated")
            else:
                return Response(serializer.errors) 


    except :
        return Response({"invalid : INVALID"})


        
