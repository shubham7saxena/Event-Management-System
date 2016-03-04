from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	# A required line - links a UserProfile to User.
	user = models.OneToOneField(User)
	
	# The additional attributes we are including.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __unicode__(self):
		return self.user.username

class event(models.Model):
	name = models.CharField(max_length=50)
	day = models.IntegerField()
	event_coordi = models.CharField(max_length=50)
	contact_id_coordinator = models.EmailField()
	event_description = models.TextField()
	participants = models.ManyToManyField(UserProfile)

	def publish(self):
		self.save()

	def __unicode__(self):
		return self.name

class notification(models.Model):
	title = models.CharField(max_length=20)
	content = models.TextField(max_length=70)
	
	def __str__(self):
		return self.title