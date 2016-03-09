from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import send_notif

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

	Actual_time=models.CharField(max_length=1,default='$',choices=Time_CHOICES,null=True)
	Actual_day=models.CharField(max_length=1,default='$',choices=Day_CHOICES,null=True)

	past_Actual_time=models.CharField(max_length=1,default='$',choices=Time_CHOICES,null=True)
	past_Actual_day=models.CharField(max_length=1,default='$',choices=Day_CHOICES,null=True)

	Venue = models.CharField(max_length=1,choices=Venue_choices,default='1')
	
	event_coordi = models.CharField(max_length=50)
	contact_id_coordinator = models.EmailField()
	event_description = models.TextField()
	participants = models.ManyToManyField(Profile)
	

	def save(self, *args, **kwargs):
		print "dsadfafsdsfdsfadsgagfgfb"
		temp = self

		super(Event, self).save(*args, **kwargs)
		print self.past_Actual_time
		print temp.Actual_time
		print "amit"

		if temp.Actual_time != self.past_Actual_time or temp.Actual_day != self.past_Actual_day  :
			u = self.participants.all()
			print u
			receivers = []
			for user in u:
				xx = User.objects.get(username = user).email
				receivers.append(xx)
			#print xx
			send_notif.sendmail_to_registered(receivers,self.name,self.event_coordi,self.contact_id_coordinator,self.Venue)



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
