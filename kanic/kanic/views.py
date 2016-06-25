import datetime

from django import forms
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from users.forms import RegisterForm
from users.models import User
from beta.models import Tester

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


# @csrf_exempt
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

# import csv
# import os
# from datetime import datetime
# def add(request):
#
#     with open(os.path.join(settings.BASE_DIR, 'kanic/products_199.csv'), 'rb') as file:
#         r = csv.reader(file, delimiter=',')
#         next(r, None)
#         car = True
#         for row in r:
#             print isinstance(row[6], str)
#
#             if row[5]=='1':
#                 car = True
#                 print car
#             else:
#                 car = False
#                 print car
#             print row[6]
#             time = date_object = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S.%f')
#             if Tester.objects.filter(email=row[2]):
#                 pass
#             else:
#                 t = Tester(name=row[1], email=row[2], phone=row[3], zipCode=row[4], car=row[5], createAt=time)
#                 t.save()
    # a = Tester.objects.all()
    # for i in a:
    #
    #     print i.createAt
    # return HttpResponse("HEHE")
