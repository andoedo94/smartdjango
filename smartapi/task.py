from background_task import background
from background_task.models import Task

from smartapi.jobs.downloadtweet import download_tweets
from smartapi.models.services.routinesTweetsService import RoutinesTweetsServices
from datetime import datetime


@background()
def routinesdaily():
    routines = RoutinesTweetsServices.get_routines()
    for routine in routines:
        active = True
        runs = routine.runs
        initial = routine.initial_date
        final = datetime.now().date()
        if routine.runs > 0:
            initial = datetime.now().date()
        if routine.final_date == datetime.now().date():
            active = False
        download_tweets(routine.city, initial, final, schedule=datetime.now(),
                        verbose_name="Download Tweet" + routine.city.name)
        RoutinesTweetsServices.update_routine(routine.id, (runs + 1), active)



