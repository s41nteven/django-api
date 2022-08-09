from django.db import models

# Create your models here.

class Lobby(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.name