from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Profile(models.Model):
	# A required line - links a UserProfile to User.
	user = models.OneToOneField(User)
	
	# The additional attributes we are including.
	phone = models.TextField(max_length=10, unique=True, blank=False, null=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	first_name = models.TextField(max_length=20, blank=False, null=True)
	last_name = models.TextField(max_length=20, blank=True, null=True)

	def UserName(self):
		return self.user.username

	def Email(self):
		return self.user.email

	def Name(self):
		return self.first_name

	def __unicode__(self):
		return self.user.username

class Event(models.Model):
	name = models.CharField(max_length=50)
	Time_CHOICES = (('0', '9:00 a.m.'),('1', '10:00 a.m.'),('2', '11:00 a.m.'),('3', '12:00 a.m.'),('4', '1:00 p.m.'),('5', '2:00 p.m.'),('6', '3:00 p.m.'),('7', '4:00 a.m.'),('8', '5:00 p.m.'),('9', '6:00 p.m.'))
	
	Day_CHOICES = (('0','Day 1'),('1','Day 2'),('2','Day 3'),('3','Day 4'))
	
	Venue_choices = (('1','Pronite Area'),('2','Basky-Court'),('3','Academic Block 1'),('4','Academic Block 2'),('5','Mall Stage'))

	first_day_preference = models.CharField(max_length=1, choices=Day_CHOICES,default='0')
	first_time_preference = models.CharField(max_length=1, choices=Time_CHOICES,default='0')
	second_day_preference = models.CharField(max_length=1, choices=Day_CHOICES,default='1')
	second_time_preference = models.CharField(max_length=1, choices=Time_CHOICES,default='1')
	third_day_preference = models.CharField(max_length=1, choices=Day_CHOICES,default='2')
	third_time_preference = models.CharField(max_length=1, choices=Time_CHOICES,default='2')

	Actual_time = ''

	Venue = models.CharField(max_length=1,choices=Venue_choices,default='1')
	
	event_coordi = models.CharField(max_length=50)
	contact_id_coordinator = models.EmailField()
	event_description = models.TextField()
	participants = models.ManyToManyField(Profile)

	def participants_list(self):
		return ", ".join([p.user.username for p in self.participants.all()])

	def register_user(self,user):
		registration = EventUserRegistration(event=self, user=user)
		registration.save()

	def publish(self):
		self.save()

	def __unicode__(self):
		return self.name


class EventUserRegistration(models.Model):
    """
    Represents a user's registration to the event.
    """
    event = models.ForeignKey(Event)
    user = models.ForeignKey(Profile)

    def __unicode__(self):
        return (self.user.__unicode__() + unicode(_(" registered for ")) +
               self.event.__unicode__())
