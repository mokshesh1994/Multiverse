from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class story_document(models.Model):

	title = models.CharField(max_length=200)
	author = models.CharField(max_length=50)
	'''
	tags = models.CharField(max_length=50)
	upvotes = models.IntegerField(default = 0)
	sub_id = models.CharField(max_length = 50)
	domain = models.CharField(max_length = 50)
	sub_reddit = models.CharField(max_length = 50)
	archived = models.BooleanField(default = True)
	over_18 = models.BooleanField(default=False)
	file_path = models.CharField(max_length=100)
	'''
	def publish(self):
		self.title = ''
		self.author = ''

	#def snippet(self):




# Create your models here.
