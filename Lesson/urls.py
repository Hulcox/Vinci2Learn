from django.urls import path
from .views import *

urlpatterns = [
    path('all/', lessons_index, name="lessons"),
    path('<slug:lessonID>', lesson_detail, name="lesson_detail"),
    path('reward/<slug:lessonID>', lesson_reward, name="lesson_reward"),
    path('create/lesson/', createLesson, name="create_lesson"),
    path('create/chapiter/', createChapiter, name="create_chapiter")
]