from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

from .models import User

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    is_mechanic = forms.BooleanField(required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        if len(password1) <= 4:
            raise forms.ValidationError("Password is too short")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            exists = User.objects.get(username=username)
            raise forms.ValidationError("This username is taken")
        except User.DoesNotExist:
            return username
        except:
            raise forms.ValidationError("There was an error, please try again or contact us")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            exists = User.objects.get(email=email)
            raise forms.ValidationError("This email is taken")
        except User.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("There was an error, please try again or contact us")

    def clean_is_mechanic(self):
        is_mechanic = self.cleaned_data.get("is_mechanic")

        if is_mechanic == True or is_mechanic == False:
            return is_mechanic
        else:
            raise forms.ValidationError("Plese choose are you a mechanic or not")



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'is_mechanic')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'first_name', 'last_name', 'is_active', 'is_admin', 'is_mechanic')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
