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
    ROOM_TYPES = [
        ('', 'Select room type'),
        ('living_room', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('kitchen', 'Kitchen'),
        ('bathroom', 'Bathroom'),
        ('office', 'Office'),
        ('commercial', 'Commercial Space'),]

    buyer_name = forms.CharField(
        label="Name",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Your name"}))
    phone_number = forms.CharField(label="Phone", max_length=50, required=True, validators=[
            RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Input correct phone number')], widget=forms.TextInput
        (attrs={"class": "form-control", "placeholder": "Your phone"}))
    room_type = forms.ChoiceField(
        label="Room type",
        choices=ROOM_TYPES,
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )
    company_name = forms.CharField(
        label="Company name",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your company name (optional)"
        })
    )
    room_area = forms.FloatField(
        label="Room area (m²)",
        required=True,
        min_value=1.0,
        max_value=1000.0,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Enter room area in square meters",
            "step": "0.1",
            "min": "1",
            "max": "1000"
        })
    )
