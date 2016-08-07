from django.contrib import admin

from .models import Tester, BetaMechanic, Newsletter, HiringJob, Job

admin.site.register(Tester)
admin.site.register(BetaMechanic)
admin.site.register(Newsletter)
admin.site.register(HiringJob)
admin.site.register(Job)
