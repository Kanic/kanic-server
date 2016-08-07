from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from beta.forms import SignUpForm, MechanicForm, NewsletterForm, HiringForm
from beta.models import Job, HiringJob
from beta.utils import (job_deserializer, job_deserializer_single,
                        job_deserializer_title_and_code)

def index(request):
    signup_form = SignUpForm()
    mechanic_form = MechanicForm()
    newsletter_form = NewsletterForm()
    context = {
        'signup_form': signup_form,
        'mechanic_form': mechanic_form,
        'newsletter_form': newsletter_form
    }
    jobs_object = Job.objects.all()
    jobs = job_deserializer_title_and_code(jobs_object)
    context['jobs'] = jobs
    template = 'index/index.html'
    return render(request, template, context)


def hiring_form(request):
    if request.method == 'GET':
        code = request.GET.get('code', None)
        if code is not None:
            context = {}
            try:
                job_object = Job.objects.get(code=code)
            except Job.DoesNotExist:
                return redirect(reverse('index-index'))
            else:
                data = {'code': code}
                form = HiringForm(initial=data)
                job = job_deserializer_single(job_object)
                context['job'] = job
                context['form'] = form
                return render(request, 'index/hiring_form.html', context)
        else:
            return redirect(reverse('index-index'))
    else:
        return redirect(reverse('index-index'))
