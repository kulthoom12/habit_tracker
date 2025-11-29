from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'description', 'completed_today', 'frequency', 'streak']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter habit title',
                'aria-label': 'Habit title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your habit',
                'aria-label': 'Habit description'
            }),
            'frequency': forms.Select(attrs={
                'class': 'form-control',
                'aria-label': 'Habit frequency'
            }),
            'completed_today': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'aria-label': 'Completed today'
            }),
        }
