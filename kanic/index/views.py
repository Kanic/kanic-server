from django.shortcuts import render
from beta.forms import SignUpForm, MechanicForm


def index(request):
    signup_form = SignUpForm()
    mechanic_form = MechanicForm()
    context = {
        'signup_form': signup_form,
        'mechanic_form': mechanic_form
    }
    template = 'index/index.html'
    return render(request, template, context)
