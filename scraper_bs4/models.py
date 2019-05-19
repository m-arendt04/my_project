from django.db import models


class BudmiexInfo(models.Model):
    invest_name = models.CharField(max_length=128)
    invest_url = models.TextField()
    invest_img_src = models.TextField()

    def __str__(self):
        return f'Information about {self.invest_name} investment.'
