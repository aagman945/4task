from django.contrib import admin
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','user')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)


