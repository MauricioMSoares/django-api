from background_task import background
from background_task.tasks import Task as BackgroundTask
from house.models import House
from task.models import COMPLETE


@background(schedule=10)
def calculate_house_stats():
    for house in House.objects.all():
        total_tasks = 0
        completed_tasks_count = 0
        house_task_lists = house.lists.all()
        for task_list in house_task_lists:
            total_tasks += task_list.tasks.count()
            completed_tasks_count += task_list.tasks.filter(status=COMPLETE).count()
        house.completed_tasks_count = completed_tasks_count
        house.notcompleted_tasks_count = total_tasks - completed_tasks_count
        house.save()


if not BackgroundTask.objects.filter(verbose_name="calculate_house_stats").exists():
    calculate_house_stats(
        repeat=BackgroundTask.DAILY, verbose_name="calculate_house_stats", priority=0
    )
