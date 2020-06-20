from django.db import models

class VideoData(models.Model):
	title = models.CharField(max_length=1000)
	description = models.CharField(max_length=1000)
	url = models.CharField(max_length=1000)
	unique_id = models.CharField(max_length=100)

# Create your models here.
