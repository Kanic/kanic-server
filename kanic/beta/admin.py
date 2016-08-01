from django.contrib import admin

from .models import Tester, BetaMechanic, Newsletter

admin.site.register(Tester)
admin.site.register(BetaMechanic)
admin.site.register(Newsletter)
