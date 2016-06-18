import datetime

from django import forms
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from users.forms import RegisterForm
from users.models import User


def index(request):
    return HttpResponse("I dream of being a web site")


class MameForm(forms.Form):
    your_name = forms.DateTimeField(initial=datetime.datetime.today)

def testform(request):
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    print request.method in SAFE_METHODS
    form = MameForm()
    context = {
        "form": form
    }
    print request.GET
    return render(request, "testform.html", context)


@csrf_exempt
def home(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password2']
        is_mechanic = form.cleaned_data['is_mechanic']
        User.objects.create_user(username=username, email=email, password=password, is_mechanic=is_mechanic)

    context = {
        "form": form,
        "action_value": "/home",
        "submit_btn_value": "register"
    }

    return render(request, "home.html", context)
