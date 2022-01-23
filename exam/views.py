from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Questions
import datetime
from exam import forms


def index(request):
    if Questions.objects.all():
        questions = Questions.objects.filter(label=True)
        learned = Questions.objects.filter(label=False)
        percent = len(learned)/(len(questions)+len(learned))
        percent2 = (len(learned)-1)/(len(questions)+len(learned))
        percent2 = round(percent2*percent*100, 2)
        percent = round(percent*100, 2)
        remains = time()
        quest = remains/len(questions)
        quest = round(quest, 2)
        return render(request, 'exam/exam_main.html', {'questions': questions, 'learned': learned, 'percent': percent,
                                                   'percent2': percent2, 'remains': remains, 'quest': quest})
    else:
        return render(request, 'exam/exam_main.html')


def time():
    time1 = datetime.datetime.now()
    time2 = datetime.datetime(2022, 2, 25)
    delta = time2 - time1
    remains = delta.total_seconds() // 60
    return remains


def edit(request, number):
    a = Questions.objects.get(question=number)
    a.label = False
    a.save()
    return redirect(index)

def edit_exam(request):
    form = forms.forms
    return render (request, 'exam/exam_edit.html', {'form': form})