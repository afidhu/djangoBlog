from django.contrib.auth.forms import UserCreationForm
from django import forms

from.models import Users, Profile

class registerForm(UserCreationForm):
    class Meta:
        model=Users
        fields=('username', 'email','password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(registerForm, self).__init__(*args, **kwargs)
        
        # Apply Bootstrap class to all fields
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
        # Remove help text for specified fields
        for fieldname in ('username', 'email', 'password1', 'password2'):
            self.fields[fieldname].help_text = None



class profileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('image',)
        widgets={
            'image':forms.FileInput(attrs={'class':'form-control'})
        }


class userupdateForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=('username', 'email',)

    def __init__(self, *args, **kwargs):
        super(userupdateForm, self).__init__(*args, **kwargs)
        
        # Apply Bootstrap class to all fields
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
        # Remove help text for specified fields
        for fieldname in ('username', 'email'):
            self.fields[fieldname].help_text = None
