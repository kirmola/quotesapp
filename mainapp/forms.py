from django import forms
from .models import SimpleContact

class SimpleContactForm(forms.ModelForm):
    
    class Meta:
        model = SimpleContact
        fields = '__all__'

        widgets = {
            "name":forms.TextInput(attrs={
                "class": "shadow-sm border text-sm rounded-lg block w-full p-2.5",
                "placeholder": "Enter your Name",
                "required":""
            }),
            "email":forms.EmailInput(attrs={
                "class":"shadow-sm border text-sm rounded-lg block w-full p-2.5",
                "placeholder": "Enter your email",
                "required":""
            }),
            "problem":forms.Select(attrs={
                "class":"block p-3 w-full text-sm rounded-lg border shadow-sm",
                "required":""
            }),
            "elaboration":forms.Textarea(attrs={
                "class":"block p-2.5 w-full text-sm rounded-lg shadow-sm border",
                "placeholder":"Explain in detail...",
                "required":""
            })
        }
