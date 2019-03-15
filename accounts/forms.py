from django import forms
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.forms.widgets import TextInput
from accounts.models import AudioFile,Button, Pad

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')


        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Benutzer existiert nicht')
            if not user.check_password(password):
                raise forms.ValidationError('Falsches Password')
            if not user.is_active:
                raise forms.ValidationError('Benutzer nicht mehr aktiv')
        return super(UserLoginForm, self).clean()

class UserRegisterForm(forms.ModelForm):
    email= forms.EmailField(label='Email Adresse')
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password'
        ]



class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ('name', 'file', )

class SettingForm(forms.ModelForm):
    def __init__(self, user_cur, *args, **kwargs):
        super(SettingForm, self).__init__(*args, **kwargs)

        current_user = user_cur

        print(current_user)
        self.fields['audio'].queryset = AudioFile.objects.filter(user=current_user)
    class Meta:
        model = Button
        exclude = ('by_user',)
        fields = ('audio', 'name', 'color', 'preset', )
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }

class PadForm(forms.ModelForm):
    def __init__(self, user_cur, *args, **kwargs):
        super(PadForm, self).__init__(*args, **kwargs)
        current_user = user_cur
        print("d")
        print(current_user)
        self.fields['buttonlist'].queryset = Button.objects.filter(user=current_user)

    class Meta:
        model = Pad
        fields = ('name','buttonlist',)