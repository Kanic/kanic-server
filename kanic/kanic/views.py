from django.shortcuts import render

from users.forms import RegisterForm
from users.models import User






def home(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password2']
        is_mechanic = form.cleaned_data['is_mechanic']
        User.objects.create_user(username=username, email=email, password=password, is_mechanic=is_mechanic)
        print username, email, password, is_mechanic


    context = {
        "form": form,
        "action_value": "/home",
        "submit_btn_value": "register"
    }

    return render(request, "home.html", context)
