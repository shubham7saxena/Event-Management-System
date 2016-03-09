from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from registeration.models import *
from registeration.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.contrib import messages
import Bpm
import send_notif
from .models import Profile, Event
import json
from django.core.serializers.json import DjangoJSONEncoder
def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

def index(request):
    context = RequestContext(request)

    if request.session.get('last_visit'):
        last_visit_time = request.session.get('last_visit')

        visits = request.session.get('visits', 0)

        if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
            request.session['visits'] = visits + 1
    else:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = 1

    if request.user.is_authenticated():
        print "***************************************************************************"
        xx = request.user.is_staff

        if xx is True:
            print "hbjeccnfnjncdnncjdhj AMit Jain \n \n \n"
            return run_bpm(request)

        else:   
            # print "***************************************************************************"
            return render_to_response('registeration/index.html', context)
    else:   
        # print "***************************************************************************"
        return render_to_response('registeration/index.html', context)

def register(request):
    context = RequestContext(request)
    context_dict = {}
    registered = False

    if request.method == 'POST':
        # Grab raw form data - making use of both FormModels.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Two valid forms?
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            # Now we can sort out the UserProfile instance.
            # We'll be setting values for the instance ourselves, so commit=False prevents Django from saving the instance automatically.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Profile picture supplied? If so, we put it in the new UserProfile.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict['user_form'] = user_form
    context_dict['profile_form']= profile_form
    context_dict['registered'] = registered

    return render_to_response(
        'registeration/register.html',
        context_dict,
        context)

def user_login(request):

    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/registeration/')
            else:
                return render_to_response('registeration/login.html', context)
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            context_dict['bad_details'] = True
            return render_to_response('registeration/login.html', context_dict, context)

    else:
        return render_to_response('registeration/login.html', context_dict, context)

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/registeration/')


@login_required
def profile(request):
    context = RequestContext(request)
    context_dict = {}
    u = User.objects.get(username=request.user)

    try:
        up = Profile.objects.get(user=u)
    except:
        up = None

    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render_to_response('registeration/profile.html', context_dict, context)



@login_required
def listview(request):
    context = RequestContext(request)
    context_dict = {}
    event_list = Event.objects.all()
    events = list(Event.objects.values_list())
    events_json = json.dumps(events,cls=DjangoJSONEncoder)
    context_dict['events'] = events_json

   # Bpm.bpm(event_list)
    return render_to_response('registeration/event_list.html',context_dict,context)


def EventDetailView(request,pk):
    context = RequestContext(request)

    x = get_object_or_404(Event, pk=pk)
    context_dict = {}
    context_dict['event'] = x

    xx = User.objects.get(username = request.user)

    userRegistered = 0

    if Event.objects.filter(participants=xx.profile,pk=pk).exists():
        userRegistered = 1
    else:
        pass

    print userRegistered    
    context_dict['userRegistered'] = userRegistered

    return render_to_response('registeration/event_detail.html',context_dict,context)


@login_required
def run_bpm(request):
    event_list = Event.objects.all()
    print "xx ----------  \n"
    print event_list
    
    count=0
    for event in event_list:
        if event.Actual_time=='$':
            count+=1


    print "xx ----------  \n"
    y = Bpm.bpm(event_list)
    print "---------------------------------------------------------------------\n "
    print y
    print "---------------------------------------------------------------------\n "
    context_dict = {}
    context_dict['events'] = event_list
    context_dict['count'] = count

    return render_to_response('registeration/indexAdmin.html',context_dict)


'''
par=event.participants.all()

for p in par
    x=User.objects.get(username = p)
    x.email
'''
@login_required
def user_register(request):
    
    xx = User.objects.get(username = request.user)
    
    print xx.profile
    pk = request.GET.get('pk', '') 
    print pk
    x = Event.objects.get(pk = pk)
    #if x.objects.filter(username=str(xx.profile)).exists():
	
    x.participants.add(xx.profile)
    x.save()
    print xx.email
    send_notif.sendmail(xx.email,xx.profile,x.name,x.event_coordi,x.contact_id_coordinator,x.Venue)
    return HttpResponse(1)
    pass

@login_required
def user_deregister(request):
    xx = User.objects.get(username = request.user)
    print xx.profile
    pk = request.GET.get('pk', '') 
    print pk
    x = Event.objects.get(pk = pk)
    x.participants.remove(xx.profile)
    x.save()
    return HttpResponse(1)
    pass
