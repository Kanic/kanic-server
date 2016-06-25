from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect

from .forms import SignUpForm


def index(request):
    form = SignUpForm(request.POST or None)
    context = {
        "form": form
    }
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Submitted successfully.')
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'beta/index.html', context)


    return render(request, 'beta/index.html', context)
