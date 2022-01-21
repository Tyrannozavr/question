from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Exam

def index(request):
    questions = Exam.objects.filter(label=True)
    learned = Exam.objects.filter(label=False)
    return render(request, 'exam/exam_main.html', {'questions': questions, 'learned': learned})

# Create your views here.
def edit(request, number):
    a = Exam.objects.get(question=number)
    a.label = False
    a.save()
    return redirect(index)