from django.db import models

# Create your models here.


class aboutdahanraj(models.Model):
   heading = models.CharField(max_length=700)
   paragraph = models.TextField()
   train_number = models.IntegerField()
   stu_num = models.IntegerField()
   expfac_num = models.IntegerField()
   course_num = models.IntegerField()