from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

from celery.schedules import crontab

import scraper_bs4.tasks as scraper_task

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

app = Celery('my_project')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_schedule_task(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=0, hour='*/3'), scraper_task.store_budimex_info.s(), name='test')
    sender.add_periodic_task(crontab(minute=0, hour='*/3'), scraper_task.store_dom_development_info.s(),
                             name='test')
    sender.add_periodic_task(crontab(minute=0, hour='*/3'), scraper_task.store_victoria_info.s(), name='test')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
