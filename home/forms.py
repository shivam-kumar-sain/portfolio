from django import forms
from .models import Project,Blog

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



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "image"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "px-4 py-3 rounded-xl border border-gray-300 "
                         "focus:ring-2 focus:ring-indigo-500 focus:outline-none "
                         "shadow-sm placeholder-black text-black",
                "placeholder": "Enter blog title",
            }),
            "content": forms.Textarea(attrs={
                "class": "px-4 py-3 rounded-xl border border-gray-300 "
                         "focus:ring-2 focus:ring-indigo-500 focus:outline-none "
                         "shadow-sm resize-none placeholder-black text-black",
                "placeholder": "Write your blog content here...",
                "rows": 6,
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "px-4 py-2 rounded-xl border border-gray-300 "
                         "focus:ring-2 focus:ring-indigo-500 focus:outline-none "
                         "shadow-sm text-black",
            }),
        }