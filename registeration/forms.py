from django import forms
from django.contrib.auth.models import User
from registeration.models import Profile


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Enter a username.")
    email = forms.CharField(help_text= "Enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Enter a password.")\

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'This email-id is already registered with us')
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    first_name = forms.CharField(help_text="Enter your first name")
    last_name = forms.CharField(help_text="Enter your last name")
    phone = forms.RegexField(regex=r'^\+?1?\d{10,12}$', error_message = ("Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed."),help_text="Please enter your phone number", required=True)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = Profile
        fields = ('first_name','last_name','phone', 'picture')