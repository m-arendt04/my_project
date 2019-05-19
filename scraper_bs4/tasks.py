from __future__ import absolute_import, unicode_literals
import os

import django
from celery import shared_task

import scraper_bs4.scrape_functions as scraper

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from .models import BudimexInfo, DomDevelopmentInfo, VictoriaInfo


@shared_task()
def store_budimex_info():
    budimex_info = scraper.scrape_budim()

    for url, img_src, title in budimex_info:
        try:
            test_obj = BudimexInfo.objects.get(invest_name=title)

        except BudimexInfo.DoesNotExist:
            new_investment = BudimexInfo()
            new_investment.invest_name = title
            new_investment.invest_img_src = img_src
            new_investment.invest_url = url
            new_investment.save()


@shared_task()
def store_dom_development_info():
    dd_info = scraper.scrape_dd()

    for url, img_src, title in dd_info:
        try:
            test_obj = DomDevelopmentInfo.objects.get(invest_name=title)

        except DomDevelopmentInfo.DoesNotExist:
            new_investment = DomDevelopmentInfo()
            new_investment.invest_name = title
            new_investment.invest_img_src = img_src
            new_investment.invest_url = url
            new_investment.save()


@shared_task()
def store_victoria_info():
    victoria_info = scraper.scrape_victoria()

    for url, img_src, title in victoria_info:
        try:
            test_obj = VictoriaInfo.objects.get(invest_name=title)

        except VictoriaInfo.DoesNotExist:
            new_investment = VictoriaInfo()
            new_investment.invest_name = title
            new_investment.invest_img_src = img_src
            new_investment.invest_url = url
            new_investment.save()
