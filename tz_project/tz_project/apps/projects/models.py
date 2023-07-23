from django.db import models
from django.utils import timezone

STATE_CHOICES = (
    ('активен', 'активен'),
    ('неактивен', 'неактивен')
)

STATUS_CHOICES = (
    ('новая', 'новая'),
    ('в работе', 'в работе'),
    ('закрыта', 'закрыта', )
)

POST_CHOICES = (
    ('junior', 'junior'),
    ('middle', 'middle'),
    ('senior', 'senior')
)

class Project(models.Model):
    project_title = models.CharField('название', max_length=100)
    project_lead = models.OneToOneField('Worker', on_delete=models.PROTECT, null=True)
    project_description = models.TextField('описание')
    project_state = models.CharField('состояние', max_length=9, choices=STATE_CHOICES, default='неактивен') # реализация выбора

    def __str__(self):
        return self.project_title
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Task(models.Model):
    source_task = models.ForeignKey('Project', on_delete=models.CASCADE)
    task_name = models.CharField('название', max_length=100)
    task_period = models.DateTimeField('срок исполнения')
    task_description = models.TextField('описание')
    task_state = models.CharField('статус', max_length=8, choices=STATUS_CHOICES, default='новая')

    def __str__(self):
        return self.task_name
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Worker(models.Model):
    worker_task = models.OneToOneField('Task', on_delete=models.PROTECT)
    worker_fio = models.CharField('ФИО', max_length=100)
    worker_post = models.CharField('должность', max_length=6, choices=POST_CHOICES)

    def __str__(self):
        return self.worker_fio
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Comment(models.Model):
    source_comm = models.ForeignKey('Project', on_delete=models.CASCADE)
    comment_text = models.TextField('текст комментария')
    comment_date = models.DateTimeField('дата публикации', default = timezone.now())

    def __str__(self):
        return self.comment_text
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'