from django import forms

class Exam(forms.Form):
    quantity_questions = forms.IntegerField(initial=100)
    date_of_examenation = forms.DateField(initial='2022-10-12 10:00:00')