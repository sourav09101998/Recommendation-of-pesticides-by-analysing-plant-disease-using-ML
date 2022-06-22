import imp
from django.contrib import admin
from .models import Inferences,Query
# Register your models here.
admin.site.register(Inferences)

admin.site.register(Query)