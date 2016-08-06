import datetime

from django import forms
from django.forms import (BooleanField, CharField, EmailField, ChoiceField,
                          FileField)
from django.forms.extras.widgets import SelectDateWidget

from .models import Tester, BetaMechanic, Newsletter, HiringJob

class SignUpForm(forms.ModelForm):
    first_name = CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name'
            })
    )
    last_name = CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name'
            })
    )
    email = EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
            })
    )
    phone = CharField(
        label="Phone\n(Optional)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone number(Optional)'
            })
    )
    zipCode = CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Zip code'
            })
    )
    car = ChoiceField(
        label="Do you own a car?",
        widget=forms.RadioSelect(attrs={
            'class': 'car-choose',
        }),
        choices=((True, 'Yes'),(False, 'No'))
    )
    hidden = CharField(
        widget=forms.HiddenInput(),
        initial='carowner'
    )

    class Meta:
        model = Tester
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'zipCode',
            'car',
            'hidden'
        ]

    def clean_name(self):
        name = (self.cleaned_data.get('name')).lower()
        return name

    def clean_email(self):
        email = (self.cleaned_data.get('email')).lower()
        if ('@' not in email) or ('.' not in email):
            raise forms.ValidationError("Must use a valid email")
        print email
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        return phone

    def clean_zipCode(self):
        zipCode = self.cleaned_data.get('zipCode')
        if zipCode.isdigit():
            return zipCode
        else:
            raise forms.ValidationError("zip code must be numbers.")

    def clean_car(self):
        car = self.cleaned_data.get('car')
        if (car in ['True', True]):
            return True
        else:
            return False

class MechanicForm(forms.ModelForm):
    first_name = CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name'
            })
    )
    last_name = CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name'
            })
    )
    email = EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
            })
    )
    phone = CharField(
        label="Phone\n(Optional)",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone number(Optional)'
            })
    )
    is_certified = ChoiceField(
        label="Are you certified?",
        widget=forms.RadioSelect,
        choices=((True, 'Yes'),(False, 'No'))
    )
    certification = CharField(
        label="If yes which certification do you have?",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Certification'
            })
    )
    work_type = ChoiceField(
        label="Are you available to work part time or full time?",
        widget=forms.RadioSelect,
        choices=(('FT', 'Full Time'),('PT', 'Part Time'))
    )
    hidden = CharField(
        widget=forms.HiddenInput(),
        initial='mechanic'
    )

    class Meta:
        model = BetaMechanic
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'is_certified',
            'certification',
            'work_type',
            'hidden'
        ]


class NewsletterForm(forms.ModelForm):
    email = EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control email',
            'placeholder': 'Your email address'
            })
    )

    class Meta:
        model = Newsletter
        fields = ['email']


class HiringForm(forms.ModelForm):
    title = CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Job title'
            })
    )
    resume = FileField()

    class Meta:
        model = HiringJob
        fields = ['title', 'resume']
