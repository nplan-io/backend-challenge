from django.db import models

# Create your models here.

class Project(models.Model):
    """ Project model """

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="")
    created = models.DateTimeField(auto_now=True)
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    product_phase = models.CharField(
        max_length=10,
        choices=WEEKDAYS,
        default=1)
    owned_by = models.ForeignKey(User, null=True,
                                 on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """ Schedule model """

    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True,
                                related_name="schedules")
    status = models.CharField(max_length=50, default="New")
    language = models.CharField(max_length=5, null=True)
    schedule_file = models.FileField(upload_to='schedule_files/', default=None)
    progress_name = models.CharField(max_length=100, default="Baseline")
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                 on_delete=models.DO_NOTHING, default=None)
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
