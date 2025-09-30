from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'project_img', 'status']
        widgets = {
            'project_name': forms.TextInput(attrs={
                'class': 'px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:outline-none shadow-sm placeholder-black text-black',
                'placeholder': 'Enter project name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:outline-none shadow-sm resize-none placeholder-black text-black',
                'placeholder': 'Enter project description',
                'rows': 4,
            }),
            'project_img': forms.ClearableFileInput(attrs={
                'class': 'px-4 py-2 rounded-xl border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:outline-none shadow-sm text-black',
            }),
            'status': forms.Select(attrs={
                'class': 'px-4 py-3 rounded-xl border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:outline-none shadow-sm text-black',
            }),
        }
