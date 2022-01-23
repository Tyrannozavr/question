from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from exam.forms import Exam
from exam.models import Exam as examenation
from exam.models import Questions as quest


def index(request):
    return HttpResponse('<h1><a href = "exam/">Main page Django</a></h1>'
                        '<h1><a href="edit/">page for edit examenation</a></h1>')


def edit(request):
    if request.POST:
        quantity_questions = request.POST.get('quantity_questions')
        date_of_examenation = request.POST.get('date_of_examenation')
        quest.objects.all().delete()
        for i in range(int(quantity_questions)):
            quest.objects.create(question=i+1, label=True)
        examenation.objects.all().delete()
        examenation.objects.create(quantity_questions=quantity_questions, time_exam=date_of_examenation)
        return HttpResponseRedirect(reverse('main'))
    return render(request, 'exam/exam_edit.html', {'form': Exam})
