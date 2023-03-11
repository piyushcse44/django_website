from django.shortcuts import render,redirect
from project_app.models import project
from project_app.form import project_form
from django.http import HttpResponse


def home(request):
    queryset = project.objects.all()
    context = {'queryset':queryset,'size':queryset.count()}
    return render(request,'project/home.html',context)


def about(request,ids):  
    try:
      project_id = project.objects.get(user_id = ids)
    except(Exception):
        return HttpResponse('INVALID PAGE') 
       
    return render(request,'project/anime.html',{'project_details':project_id})


def nav(request):
    return render(request,'project/index.html')


def create_form(request):
    form = project_form()
    if(request.method=="POST"):
        form = project_form(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('homepage')
    content = {'form':form}
    return render(request,'project/project_form.html',content)


def update_form(request,ids):
    try:
        projects = project.objects.get(user_id = ids)
    except(Exception):
        return HttpResponse('INVALID PAGE') 
    form = project_form(instance=projects)
    if(request.method=='POST'):
        form = project_form(request.POST,instance=projects)
        if(form.is_valid()):
            form.save()
            return redirect('homepage')
    content = {'form':form}
    return(render(request,'project/project_form.html',content))                
    

def delete_form(request,ids):
    try:
        projects = project.objects.get(user_id = ids)
    except(Exception):
        return HttpResponse('INVALID PAGE') 
    if(request.method=='POST'):
        projects.delete()
        return redirect('homepage')
    return(render(request,'project/delete_project.html',{'project':projects}))  
