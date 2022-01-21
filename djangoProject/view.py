from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1><a href = "exam/">Main page Django</a></h1>')