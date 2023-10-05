from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=300)
    is_done = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'task'
        ordering = ['-id']

class Deadline(models.Model):
    task = models.ForeignKey(Task, related_name='deadlines', on_delete=models.CASCADE)

    date = models.DateField()
    description = models.CharField(max_length=30)
    priority = models.IntegerField(default=1)

    class Meta:
        db_table = 'deadline'
        ordering = ['priority']