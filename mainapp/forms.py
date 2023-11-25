from django import forms
from .models import SimpleContact

class SimpleContactForm(forms.ModelForm):
    
    class Meta:
        model = SimpleContact
        fields = '__all__'
