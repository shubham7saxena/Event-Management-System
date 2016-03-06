from django.template import RequestContext
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
from .models import Profile, Event

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
def events(request):
    context = RequestContext(request)
    context_dict = {}
    event_list = Event.objects.all()
    context_dict['events'] = event_list
	
    return render_to_response('registeration/events.html',context_dict,context)


@login_required
def listview(request):
    context = RequestContext(request)
    context_dict = {}
    event_list = Event.objects.all()
    context_dict['events'] = event_list
    Bpm.bpm(event_list)
    return render_to_response('registeration/event_list.html',context_dict,context)



class EventDetailView(DetailView):

    model = Event
    context_object_name = 'event'



class EventUserRegisterView(RedirectView):

    default_return_view = 'events_event_list'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        event = Event.objects.get(pk=kwargs['event_id'])

        # Check if user is not already registered
        registrations = EventUserRegistration.objects.filter(
            user=request.user,
            event=event).count()

        if registrations:
            message = _('You are already registered to the %s') % event
            messages.add_message(request, messages.ERROR, message)
            return super(EventUserRegisterView, self).dispatch(request,
                                                               *args,
                                                               **kwargs)


        registration = EventUserRegistration(user=request.user, event=event)
        registration.save()

        message = _('Successfully registered to the %s') % event
        messages.add_message(request, messages.INFO, message)

        return super(EventUserRegisterView, self).dispatch(request,
                                                           *args, **kwargs)

def user_register(request):
    xx = User.objects.get(username = request.user)
    
    print xx.profile
    pk = request.GET.get('pk', '') 
    print pk
    x = Event.objects.get(pk = pk)
    x.participants.add(xx.profile)
    x.save()
    return HttpResponse(1)
    pass