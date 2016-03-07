from django.core.mail import EmailMessage

def sendmail(email,name,event_name,coordi,contact,venue):
	realvenue=""
	if(venue==1):
		realvenue = "Pronite-Area"
	if(venue==2):
		realvenue = "Basky Court"
	if(venue==3):
		realvenue = "Academic Block-1"
	if(venue==4):
		realvenue = "Academic Block-2"
	if(venue==5):
		realvenue = "Mall Stage"
	
		
	email = EmailMessage('Congratulations for Successful Registration!!!', 'Dear '+str(name)+'\nYou have Successfully registered for the event '+event_name+'\nThe Venue for the event is : '+realvenue+'\nFor any further queries regarding to the event you may contact '+coordi+' at '+contact+'\nRegards\n Team Ignus', to=[email])
	email.send()
