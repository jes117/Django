from django.contrib import admin

# Register your models here.
from .models import Candidate,Poll

admin.site.register(Candidate)
admin.site.register(Poll)