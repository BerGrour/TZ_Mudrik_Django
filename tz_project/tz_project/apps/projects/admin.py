from django.contrib import admin

from . models import Project, Comment, Task, Worker

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'project_state')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'comment_date')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_period', 'task_state')

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('worker_fio', 'worker_post')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Worker, WorkerAdmin)