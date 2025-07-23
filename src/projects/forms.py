from django.forms import ModelForm
from django import forms
from projects.models import Project


base_class = 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'

class OrderProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'ppt_presentation', 'tech_card']
        labels = {
            'title': 'عنوان المشروع',
            'description': 'وصف المشروع',
            'type': 'نوع المشروع',
            'ppt_presentation': 'هل تريد  عرض تقديمي خاصة بالمشروع؟',
            'tech_card': 'هل تريد بطاقة تقنية خاصة بالمشروع؟',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': base_class,
                'placeholder': 'عنوان المشروع'
            }),
            'description': forms.Textarea(attrs={
                'class': base_class,
                'placeholder': 'وصف المشروع',
                'rows': 4,
                'cols': 40
            }),
            'type': forms.Select(attrs={
                'class': base_class + ' px-10',
            }),
            'ppt_presentation': forms.CheckboxInput(attrs={
                'class': 'mx-2 my-2'
            }),
            'tech_card': forms.CheckboxInput(attrs={
                'class': 'mx-2 my-2'
            }),
        }