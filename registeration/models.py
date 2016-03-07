from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Profile(models.Model):
	# A required line - links a UserProfile to User.
	user = models.OneToOneField(User)
	
	#Email = user.email
	# The additional attributes we are including.
	phone = models.TextField(max_length=10, unique=True, blank=False, null=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __unicode__(self):
		return self.user.username

	def UserName(self):
		return self.user.username

	def Email(self):
		return self.user.email

class Event(models.Model):
	name = models.CharField(max_length=50)
	Time_CHOICES = (('01', 'Day 1, 9:00am'),('02', 'Day 1, 11:00am'),('03', 'Day 1, 1:00pm'),('04', 'Day 1, 3:00pm'),('05', 'Day 1, 5:00pm'),('11', 'Day 2, 9:00am'),('12', 'Day 2, 11:00am'),('13', 'Day 2, 1:00pm'),('14', 'Day 2, 3:00pm'),('15', 'Day 2, 5:00pm'))

	first_time_preference = models.CharField(max_length=2, choices=Time_CHOICES,default='1')

	second_time_preference = models.CharField(max_length=2, choices=Time_CHOICES,default='2')

	third_time_preference = models.CharField(max_length=2, choices=Time_CHOICES,default='3')

	Actual_time = ''
	event_coordi = models.CharField(max_length=50)
	contact_id_coordinator = models.EmailField()
	event_description = models.TextField()
	participant = models.ManyToManyField(Profile)

	def participants_list(self):
		return ", ".join([p.user.username for p in self.participant.all()])

	def publish(self):
		self.save()

	def __unicode__(self):
		return self.name

