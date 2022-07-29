from django.db import models

# Create your models here.


class Qaydlar(models.Model):
    qayd_name = models.CharField(max_length=11)
    reg_Time = models.TimeField()
    maqsad = models.CharField(max_length=40)
    muhim = models.CharField(max_length=15)
    def __str__(self):
        return self.qayd_name