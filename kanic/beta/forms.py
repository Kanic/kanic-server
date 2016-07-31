import datetime

from django import forms
from django.forms import BooleanField, CharField, EmailField, ChoiceField
from django.forms.extras.widgets import SelectDateWidget

from .models import Tester, BetaMechanic

class SignUpForm(forms.ModelForm):
    name = CharField(
        widget=forms.TextInput(attrs={'placeholder': 'David Ma'})
    )
    email = EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'David@gmail.com'})
    )
    phone = CharField(
        label="Phone\n(Optional)",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '2203333399'})
    )
    zipCode = CharField(
        widget=forms.TextInput(attrs={'placeholder': '11373'})
    )
    car = ChoiceField(
        label="Own a car?",
        widget=forms.RadioSelect,
        choices=((True, 'Yes'),(False, 'No'))
    )
    hidden = CharField(
        widget=forms.HiddenInput(),
        initial='carowner'
    )

    class Meta:
        model = Tester
        fields = ['name', 'email', 'phone', 'zipCode', 'car', 'hidden']

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
    phone = CharField(
        label="Phone(Optional)",
        required=False
    )
    is_certified = ChoiceField(
        label="Are you certified?",
        widget=forms.RadioSelect,
        choices=((True, 'Yes'),(False, 'No'))
    )
    certification = CharField(
        label="If yes which certification do you have?",
        required=False
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
        fields = ['first_name', 'last_name', 'email', 'phone', 'is_certified', 'certification', 'work_type', 'hidden' ]

    def __init__(self, *args, **kwargs):
        super(MechanicForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "mechanic-form"
        self.helper.form_method = 'post'
        self.helper.form_action = '/'
