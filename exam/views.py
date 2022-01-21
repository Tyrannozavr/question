from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Exam
import datetime

def index(request):
    questions = Exam.objects.filter(label=True)
    learned = Exam.objects.filter(label=False)
    percent = len(learned)/(len(questions)+len(learned))
    percent2 = (len(learned)-1)/(len(questions)+len(learned))
    percent2 = round(percent2*percent*100, 2)
    percent = round(percent*100, 2)
    remains = time()
    quest = remains/len(questions)
    quest = round(quest, 2)
    return render(request, 'exam/exam_main.html', {'questions': questions, 'learned': learned, 'percent': percent,
                                                   'percent2': percent2, 'remains': remains, 'quest': quest})



def time():
    time1 = datetime.datetime.now()
    time2 = datetime.datetime(2022, 2, 25)
    delta = time2 - time1
    remains = delta.total_seconds() // 60
    return remains
# Create your views here.
def edit(request, number):
    a = Exam.objects.get(question=number)
    a.label = False
    a.save()
    return redirect(index)