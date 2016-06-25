import base64

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from .forms import SignUpForm
from .models import Tester


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

def listTester(request):
    uname = "ahmed"
    pword = "123"

    if 'HTTP_AUTHORIZATION' in request.META:
        basic, auth = request.META['HTTP_AUTHORIZATION'].split()
        username, password = base64.b64decode(auth).split(':')
        if username == uname and password == pword:
            testers = Tester.objects.all().order_by('-createAt')
            total = testers.count()

            context = {
                "testers": testers,
                "total": total
            }
            return render(request, 'beta/listTester.html', context)

    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="%s"' % "Basci Auth Protected"
    return response
