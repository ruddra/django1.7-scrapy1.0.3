import os
import sys

DJANGO_PROJECT_PATH = '/Users/arnabkumarshil/ProjectsPersonal/django1.7+scrapy/example_project'
DJANGO_SETTINGS_MODULE = 'example_project.settings' #Assuming your django application's name is example_project

sys.path.insert(0, DJANGO_PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
BOT_NAME = 'example_bot'

SPIDER_MODULES = ['example_bot.spiders']

ITEM_PIPELINES = {
    'example_bot.pipelines.ExPipeline': 1000,
}

