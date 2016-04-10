
import smtplib

sender = 'ug201310005@iitj.ac.in'
receivers = ['ug201310001@iitj.ac.in']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except :
   print "Error: unable to send email"
