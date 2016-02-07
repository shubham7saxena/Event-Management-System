from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from registeration.models import UserProfile
from registeration.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect

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
            return render_to_response('registeration/login.html', context)

    else:
        return render_to_response('registeration/login.html', context)

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/registeration/')


@login_required
def profile(request):
    context = RequestContext(request)
    u = User.objects.get(username=request.user)
    
    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None
    
    return render_to_response('registeration/profile.html', context)

def track_url(request):
    context = RequestContext(request)
    page_id = None
    url = '/registeration/'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views + 1
                page.save()
                url = page.url
            except:
                pass

    return redirect(url)
