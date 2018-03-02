
from django import forms
from .models import Cats, Dogs, Owner
from django.contrib.auth.forms import AuthenticationForm 

# Create yourforms here.

class CatsForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ('name', 'birthday', 'ownerid')

class DogsForm(forms.ModelForm):
      class Meta:
        model = Dogs
        fields = ('name', 'birthday', 'ownerid')
        
class OwnersForm(forms.Form):
   class Meta:
        model = Owner
        fields = ('name')
        

                               