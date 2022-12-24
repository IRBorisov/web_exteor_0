from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def index(request):
    data = {'title': "Главная страница",
            'values': ['some', 'hello', 123],
            'obj': {'car': 'BMW', 'age': 42, 'hobby': 'football'}}
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')