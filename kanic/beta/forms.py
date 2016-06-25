import datetime

from django import forms
from django.forms import BooleanField, CharField
from django.forms.extras.widgets import SelectDateWidget

from crispy_forms.helper import FormHelper

from .models import Tester

class SignUpForm(forms.ModelForm):
    name = CharField(
        widget=forms.TextInput(attrs={'placeholder': 'David Ma'})
    )
    email = CharField(
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
    car = BooleanField(
        label="Do you have a car?",
        required=False
    )

    class Meta:
        model = Tester
        fields = ['name', 'email', 'phone', 'zipCode', 'car']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "sign-up-form"
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/'
        self.helper.label_class = 'col-bg-2 col-mid-2 col-sm-3 col-xs-3'
        self.helper.field_class = 'col-bg-8 col-mid-8 col-sm-8 col-xs-8'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if ('@' not in email) or ('.' not in email):
            raise forms.ValidationError("Musr use a valid email")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        return phone
