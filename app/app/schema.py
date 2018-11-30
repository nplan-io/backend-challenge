from app.app.tasks import process_schedule
import app.app.models as mod


# Write your unit test here using PyTest.

class ProjectType(DjangoObjectType):
    """ Django object type for returning Projects to the user """

    class Meta:
        """ Uses the Project model defined in models.py """
        model = mod.Project


class ScheduleType(DjangoObjectType):
    """ Django object type for returning Schedules to the user """

    class Meta:
        """ Uses the Schedule model defined in models.py """
        model = mod.Schedule


class TaskType(DjangoObjectType):
    """ Django object type for returning Tasks to the user """

    class Meta:
        """ Uses the Task model defined in models.py """
        model = mod.Task
