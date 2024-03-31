# Generated by Django 5.0.3 on 2024-03-31 03:11

import django.db.models.deletion
import task.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
        ('task', '0001_initial'),
        ('users', '0002_profile_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('data', models.FileField(upload_to=task.models.GenerateAttachmentFilePath())),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='task.task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('NC', 'Not Completed'), ('C', 'Completed')], default='NC', max_length=2)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lists', to='users.profile')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='house.house')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task.tasklist'),
            preserve_default=False,
        ),
    ]
