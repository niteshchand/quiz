from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'quiz/index.html', {'title':'index'})

def about(request):
    return render(request,'quiz/about.html', {'title':'about'})

def class12(request):
    return render(request,'quiz/class12.html', {'title':'class12'})

def class11(request):
    return render(request,'quiz/class11.html', {'title':'class11'})
def class10(request):
    return render(request,'quiz/class10.html', {'title':'class10'})
def class9(request):
    return render(request,'quiz/class9.html', {'title':'class9'})
def start(request):
    return render(request,'quiz/start.html', {'title':'start'})
def quiz(request):
    return render(request,'quiz/quiz.html', {'title':'quiz'})

def class12quiz(request):
    return render(request,'quiz/class12quiz.html', {'title':'class12quiz'})