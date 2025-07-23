import django_filters
from django.forms import TextInput, Select, DateInput
from .models import Project

base_class = 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'

class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='عنوان المشروع',
        widget=TextInput(attrs={
            'class': base_class,
            'placeholder': 'ابحث عن عنوان المشروع...'
        })
    )
    state = django_filters.ChoiceFilter(
        field_name='state',
        choices=[
            ('inprogress', 'قيد التنفيذ'),
            ('completed', 'مكتمل'),
            ('pending', 'معلق')
        ],
        label='حالة المشروع',
        widget=Select(attrs={
            'class': base_class + ' px-6',
        })
    )
    created_at = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='exact',
        label='تاريخ الإنشاء',
        widget=DateInput(attrs={
            'class': base_class,
            'type': 'date'
        })
    )

    class Meta:
        model = Project
        fields = ['title', 'state', 'created_at']