from django import forms
from .models import OurProjects


class CardProjectForm(forms.ModelForm):
    class Meta:
        model = OurProjects
        fields = ['project_image', 'project_description']
        widgets = {
            'project_description': forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Опишите проект", "rows": 4}),
            'project_image': forms.FileInput(attrs={"class": "form-control-file"})}
        labels = {'project_image': 'Изображение проекта', 'project_description': 'Описание проекта'}
