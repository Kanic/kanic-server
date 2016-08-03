import base64

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, HttpResponseRedirect

from .forms import SignUpForm, MechanicForm, NewsletterForm, HiringForm
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
            form.save()
            return render(request, 'beta/success.html')
        else:
            print 'form is not valid'
            context['mechanic_form'] = MechanicForm()
            context['carOwner_invalid'] = 'carOwner_invalid'
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
            form.save()
            return render(request, 'beta/success.html')
        else:
            print "form is not valid"
            context['signup_form'] = SignUpForm()
            context['mechanic_invalid'] = 'mechanic_invalid'
            return render(request, 'index/index.html', context)

    return HttpResponseRedirect(reverse('index-index'))


def newsletter_signup(request):
    """
    Method: POST
    Description: Create sign up for newsletter
    """
    form = NewsletterForm()
    context = {
        'newsletter_form': form
    }
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        context['newsletter_form'] = form
        if form.is_valid():
            form.save()
            return render(request, 'beta/success.html')
        else:
            print "form is not valid"
            context['signup_form'] = SignUpForm()
            context['mechanic_form'] = MechanicForm()
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


def hiring_signup(request):
    form = HiringForm()
    context = {
        'hiring_form': form
    }
    if request.method == 'POST':
        form = HiringForm(request.POST, request.FILES)
        context['hiring_form'] = form
        if form.is_valid():
            form.save()
            return render(request, 'beta/success.html')
        else:
            print "form is not valid"
            return render(request, 'index/hiring_form.html', context)

    return HttpResponseRedirect(reverse('index-index'))
