from django.contrib import admin
from {{ app_name }}.models import *

# Register your models here

# For more information on this file, see
# https://docs.djangoproject.com/en/{{ docs_version }}/intro/tutorial02/

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
 
class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
 
admin.site.register(Poll, PollAdmin)