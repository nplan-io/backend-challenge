from django.db import models

# Create your models here.

class Project(models.Model):
    """ Project model """

    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    uid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """ Schedule model """

    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True,
                                related_name="schedules")
    status = models.CharField(max_length=50, default="New")
    schedule_file = models.FileField(upload_to='schedule_files/', default=None)
    deadline = models.DateTimeField(default=None, null=True)



class Task(models.Model):
    """ Task model """

    name = models.CharField(max_length=200)
    task_id = models.CharField(max_length=20, default="")
    start = models.DateTimeField(default=None, null=True)
    end = models.DateTimeField(default=None)
    calendar = models.ForeignKey(
        Calendar, on_delete=models.DO_NOTHING, default=None, null=True,
        related_name="tasks")

class Calendar(models.Model):
    """ Calendar model """

    name = models.CharField(max_length=100)
    calendar_id = models.CharField(max_length=20)


    def __str__(self):
        return self.name
