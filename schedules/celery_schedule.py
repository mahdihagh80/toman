CELERY_BEAT_SCHEDULE = {}

JOBS = [
    {
        'name': 'delete_invalid_images',
        'task': 'shop.tasks.delete_invalid_images',
        'schedule': 30,
        'workers': 2
    },
]


for job in JOBS:
    for worker_id in range(job['workers']):
        name = job['name'] + str(worker_id)
        CELERY_BEAT_SCHEDULE[name] = {
            'task': job['task'],
            'schedule': job['schedule'],
            'args': (job['workers'], worker_id,),
        }
