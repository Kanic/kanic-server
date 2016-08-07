from django.conf import settings
from django.core.mail import EmailMessage

def job_deserializer_single(job):
    data = {
        'title': job.title,
        'code': job.code,
        'requirement': job.get_requirement,
        'responsibility': job.get_responsibility,
        'description': job.description,
        'type': job.type,
        'salary': job.salary
    }

    return data


def job_deserializer(jobs):
    data = []
    for job in jobs:
        single = {
            'title': job.title,
            'code': job.code,
            'requirement': job.get_requirement,
            'responsibility': job.get_responsibility,
            'description': job.description,
            'type': job.type,
            'salary': job.salary
        }
        data.append(single)

    return data


def job_deserializer_title_and_code(jobs):
    data = []
    for job in jobs:
        single = {
            'title': job.title,
            'code': job.code,
        }
        data.append(single)

    return data


def handle_uploaded_file(file):
    with open(settings.MEDIA_ROOT) as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def email_job_applied(job_title, resume):
    subject = 'Apply for {0}'.format(job_title)
    message = 'Some one applied for {0}'.format(job_title)
    fromAddress = 'kanicHR@kanic.com'
    toAddress = ['dongliang3571@gmail.com', 'ahmedbnms@gmail.com']
    email = EmailMessage(subject, message, fromAddress, toAddress)
    attach_name = resume.name
    data = ''
    for chunk in resume.chunks():
        data = data + chunk
    email.attach(attach_name, data)
    email.send()
