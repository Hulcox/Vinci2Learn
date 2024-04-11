from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def lessons_index(request):
  if not request.user.is_authenticated:
    return redirect("home")
  
  context={"lessons": Lesson.objects.all()}
  return render(request, "lessons_index.html", context=context)

def lesson_detail(request, lessonID):
  if not request.user.is_authenticated:
    return redirect("home")

  chapiters = Chapiter.objects.filter(lesson__pk=lessonID)
  lesson = chapiters[0]
  context={"chapiters":chapiters, "lesson": lesson.lesson }
  return render(request, "lesson_detail.html", context=context)

def lesson_reward(request, lessonID):
  if not request.user.is_authenticated:
    return redirect("home")

  try:
    lesson = get_object_or_404(pk=lessonID, klass=Lesson)
    return render(request, "lesson_reward.html", context={'lesson': lesson})
  except:
    lesson = None
    return HttpResponse("<h1>Lesson non trouvé !</h1>")