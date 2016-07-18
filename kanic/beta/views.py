import base64

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from .forms import SignUpForm, MechanicForm
from .models import Tester, BetaMechanic


def index(request):
    form = SignUpForm()
    mechanic_form = MechanicForm()
    context = {
        'form': form,
        'mechanic_form': mechanic_form
    }
    if request.method == 'POST':
        if request.POST.get('hidden') == 'carowner':
            form = SignUpForm(request.POST)
            context['form'] = form

            if form.is_valid():
                instance = form.save()
                messages.success(request, 'Submitted successfully.')
                return HttpResponseRedirect(reverse('index'))
            else:
                context["carOwner_invalid"] = "carOwner_invalid"
                return render(request, 'beta/index.html', context)
        elif request.POST.get('hidden') == 'mechanic':
            print("inside mechanic")
            mechanic_form = MechanicForm(request.POST)
            context['mechanic_form'] = mechanic_form

            if mechanic_form.is_valid():
                instance = mechanic_form.save()
                messages.success(request, 'Submitted successfully.')
                return HttpResponseRedirect(reverse('index'))
            else:
                context["mechanic_invalid"] = "mechanic_invalid"
                return render(request, 'beta/index.html', context)

    return render(request, 'beta/index.html', context)

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
