from django.http import HttpResponse

def index(request):
    return HttpResponse('this is the first ever view I have made with Django')
