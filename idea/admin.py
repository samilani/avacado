from django.contrib import admin
from idea.models import Idea



class AdminIdea(admin.ModelAdmin):
    list_display = ('title','owner')

admin.site.register(Idea, AdminIdea)