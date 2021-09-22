from django.contrib import admin

# Register your models here.
from myapp.models import Cohort, Native, Thought

admin.site.register(Cohort)
admin.site.register(Native)
admin.site.register(Thought)
