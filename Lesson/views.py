from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.
def lessons_index(request):
  if not request.user.is_authenticated:
    return redirect("home")
  
  context={"lessons": Lesson.objects.all()}
  return render(request, "lessons_index.html", context=context)

def lesson_detail(request, lessonID):
  if not request.user.is_authenticated:
    return redirect("home")
  try:
    chapiters = Chapiter.objects.filter(lesson__pk=lessonID)
    lesson = chapiters[0]

    lesson_completed_cookie = 'lesson_completed_{}'.format(lessonID)

    context={"chapiters":chapiters, "lesson": lesson.lesson, "lessonCompleted": request.COOKIES.get(lesson_completed_cookie)}
    return render(request, "lesson_detail.html", context=context)
  except:
    return render(request, "error.html", context={"error": "Cours non trouvé !"})
  
def lesson_reward(request, lessonID):
    if not request.user.is_authenticated:
        return redirect("home")
    
    lesson = get_object_or_404(pk=lessonID, klass=Lesson)
    lesson_completed_cookie = 'lesson_completed_{}'.format(lessonID)

    print(request.COOKIES.get(lesson_completed_cookie))

    # Vérifiez si le cookie de la leçon complétée est déjà présent
    if not request.COOKIES.get(lesson_completed_cookie):
        request.user.xp += lesson.xp_reward

        userLevelUp = False
        if request.user.xp >= request.user.level * 100:
            request.user.level += 1
            userLevelUp= True
        request.user.save()

        # Définissez le cookie pour indiquer que la leçon a été complétée
        response = render(request, "lesson_reward.html", context={'lesson': lesson,"lessonCompleted": False, "userLevelUp": userLevelUp})
        response.set_cookie(lesson_completed_cookie, 'true')
        return response
    else:
        # La leçon a déjà été complétée, redirigez simplement vers la page de récompense
        return render(request, "lesson_reward.html", context={'lesson': lesson,"lessonCompleted": True, "userLevelUp": False, })