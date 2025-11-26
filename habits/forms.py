from django.shortcuts import forms
from .models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'description', 'completed']
