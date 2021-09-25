from django.contrib import admin

# Register your models here.
from myapp.models import Cohort, Native, Thought

admin.site.register(Cohort)
admin.site.register(Native)
admin.site.register(Thought)


def getSCV(self):
    scv = f'SCV{Native.pk}0'
    return scv