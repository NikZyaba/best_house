from django import forms
from django.core.validators import RegexValidator


class ConsultingForm(forms.Form):
    buyer_name = forms.CharField(label="Name", max_length=50, required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}))
    phone_number = forms.CharField(label="Phone", max_length=50, required=True,
                                   validators=[
                                       RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Input correct phone number')],
                                   widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your phone"}))
    description = forms.CharField(label="Description", max_length=4000, required=False,
                                  widget=forms.Textarea(attrs={"class": "form-control",
                                                               "placeholder": "Ask a question or describe your project"}))


class CalculatingProjectForm(forms.Form):
    buyer_name = forms.CharField(label="Name", max_length=50, required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}))
    phone_number = forms.CharField(label="Phone", max_length=50, required=True,
                                   validators=[
                                       RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Input correct phone number')],
                                   widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your phone"}))
    room_type = forms.ChoiceField(label="Room type",
                                  choices=[("Type 1", "Тип 1"), ("Type 2", "Тип 2"), ("Type 3", "Тип 3"),
                                           ("Type 4", "Тип 4"),
                                           ("Type 5", "Тип 5"), ("Type 6", "Тип 6"), ("Type 7", "Тип 7"),
                                           ("Type 8", "Тип 8")],
                                  required=True,
                                  widget=forms.SelectMultiple(attrs={"class": "form-control", "size": "4"}))
    company_name = forms.CharField(label="Company name", max_length=100, required=False,
                                   widget=forms.TextInput(
                                       attrs={"class": "form-control", "placeholder": "Your company name"}))
