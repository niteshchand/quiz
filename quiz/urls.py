from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="quiz-index"),
    path('about/', views.about, name="quiz-about"),
    path('class12/', views.class12, name="quiz-class12"),
    path('class12quiz/', views.class12quiz, name="quiz-class12quiz"),
    path('class11/', views.class11, name="quiz-class11"),
    path('class10/', views.class10, name="quiz-class10"),
    path('class9/', views.class9, name="quiz-class9"),
    path('start/', views.start, name="quiz-start"),
    path('quiz-quiz/', views.quiz, name="quiz-quiz")

]