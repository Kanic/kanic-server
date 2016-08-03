from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from beta.forms import SignUpForm, MechanicForm, NewsletterForm, HiringForm


def index(request):
    signup_form = SignUpForm()
    mechanic_form = MechanicForm()
    newsletter_form = NewsletterForm()
    context = {
        'signup_form': signup_form,
        'mechanic_form': mechanic_form,
        'newsletter_form': newsletter_form
    }
    template = 'index/index.html'
    return render(request, template, context)


def hiring_form(request, title):
    titles = ['ios', 'android', 'web', 'marketing']
    if title in titles:
        title_str = title.lower()
        data = {
            'title': title_str
        }
        form = HiringForm(initial=data)
        context = {
            'hiring_form': form
        }
        return render(request, 'index/hiring_form.html', context)
    else:
        return HttpResponseRedirect(reverse('index-index'))
