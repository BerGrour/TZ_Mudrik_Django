# Generated by Django 4.2.3 on 2023-07-22 16:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_comment_comment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100, verbose_name='название')),
                ('task_period', models.DateTimeField(verbose_name='срок исполнения')),
                ('task_description', models.TextField(verbose_name='описание')),
                ('task_state', models.CharField(choices=[('новая', 'новая'), ('в_работе', 'в работе'), ('закрыта', 'закрыта')], default='новая', max_length=8, verbose_name='статус')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 22, 16, 25, 33, 462953, tzinfo=datetime.timezone.utc), verbose_name='дата публикации'),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('worker_post', models.CharField(choices=[('junior', 'junior'), ('middle', 'middle'), ('senior', 'senior')], max_length=6, verbose_name='должность')),
                ('worker_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.task')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='source_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]