from django import forms
from .models import *

class LessonForm(forms.ModelForm):
    class Meta():
        model = Lesson
        fields = ['title', 'description', 'author', 'dificulty', 'xp_reward']

class ChapiterForm(forms.ModelForm):
    class Meta():
        model = Chapiter
        fields = ['title', 'content', 'lesson']