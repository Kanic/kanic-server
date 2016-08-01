import base64

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from .forms import SignUpForm, MechanicForm
from .models import Tester, BetaMechanic


def car_owner_signup(request):
    """
    Method: POST
    Description: Create beta user for car owners
    """
    form = SignUpForm()
    context = {
        'signup_form': form,
        }
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        context['signup_form'] = form
        if form.is_valid():
            instance = form.save()
            return render(request, 'beta/success.html')
        else:
            print "form is not valid"
            context["carOwner_invalid"] = "carOwner_invalid"
            return render(request, 'index/index.html', context)

    return HttpResponseRedirect(reverse('index-index'))



def mechanic_signup(request):
    """
    Method: POST
    Description: Create beta user for mechanics
    """
    form = MechanicForm()
    context = {
        'mechanic_form': form,
        }
    if request.method == 'POST':
        form = MechanicForm(request.POST)
        context['mechanic_form'] = form
        if form.is_valid():
            instance = form.save()
            return render(request, 'beta/success.html')
        else:
            print "form is not valid"
            context["mechanic_invalid"] = "mechanic_invalid"
            return render(request, 'index/index.html', context)

    return HttpResponseRedirect(reverse('index-index'))


def listTester(request):
    uname = "ahmed"
    pword = "123"

    if 'HTTP_AUTHORIZATION' in request.META:
        basic, auth = request.META['HTTP_AUTHORIZATION'].split()
        username, password = base64.b64decode(auth).split(':')
        if username == uname and password == pword:
            carOwners = Tester.objects.all().order_by('-createAt')
            carOwner_total = carOwners.count()
            mechanics = BetaMechanic.objects.all().order_by('-createAt')
            mechanic_total = mechanics.count()

            context = {
                "carOwners": carOwners,
                "mechanics": mechanics,
                "carOwner_total": carOwner_total,
                "mechanic_total": mechanic_total
            }
            return render(request, 'beta/listTester.html', context)

    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="%s"' % "Basci Auth Protected"
    return response
