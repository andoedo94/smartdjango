from background_task.models import Task
from smartapi.models.models import Routine


class RoutinesTweetsServices:

    @classmethod
    def get_routines(cls):
        routines = Routine.objects.filter(active=True)
        return routines

    @classmethod
    def update_routine(cls, id, runs, active):
        routine = Routine.objects.get(pk=id)
        if routine is not None:
            routine.runs = runs
            routine.active = active
            routine.save()


