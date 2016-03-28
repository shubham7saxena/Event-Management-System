Event-Management System
------------------------

This is a simple software built over Django to manage your events systematically and punctually. It automatically schedules your events and also notifies the participants so that they are always updated. With its modularised control and admin tools, it makes it very easy to filter stuff.

Requirements:- 
--------------

Python 2.7 or any related version
Django 1.7+

Build Instructions:- 
--------------------

Run "python manage.py makemigrations" to update table structure change.
    "python manage.py migrate" to update the data according to the new database structure.
    "python manage.py runserver" to run the django https server at the default host


File Structure
--------------

As with the standard django projects, the project runs on a MVC structure with models 'models.py', views in 'views.py' and controller files that is urls  in "templates" directory. Additional files viz. 'forms.py' have been added to manage forms for the registeration and login separately and 'send_notif.py' for sending scheduled mail to the registered participants.


Features to be Added:-
----------------------
profile deletion and updating
classifying events
