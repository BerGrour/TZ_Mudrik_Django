from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:project_id>/', views.s_number, name = 's_number'),
    path('<int:project_id>/add_comment/', views.add_comment, name = 'add_comment')
]