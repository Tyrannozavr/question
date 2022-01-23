from django.contrib import admin
from .models import *

class AdminExam(admin.ModelAdmin):
    list_display = ['question', 'label']
    fields = [('question', 'label')]

admin.site.register(Questions, AdminExam)

@admin.register(Exam)
class AdminExam(admin.ModelAdmin):
    list_display = ['quantity_questions', 'time_exam']

