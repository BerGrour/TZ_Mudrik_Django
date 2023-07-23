from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . models import Project

def index(request):
    latest_projects_list = Project.objects.order_by('project_title')
    return render(request, 'projects/list.html', {'latest_projects_list': latest_projects_list})

def s_number(request, project_id):
    try:
        a = Project.objects.get(id = project_id)
    except:
        raise Http404("Проект на найден")
    
    list_comment = a.comment_set.order_by('-id')

    list_tasks = a.task_set.all()

    return render(request, 'projects/s_number.html', {'project': a, 'list_comment': list_comment, 'list_tasks': list_tasks})

def add_comment(request, project_id):
    try:
        a = Project.objects.get(id = project_id)
    except:
        raise Http404("Проект на найден")

    a.comment_set.create(comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('projects:s_number', args=(a.id,)) )
