from django import forms

class SimpleContactForm(forms.Form):
    your_name = forms.CharField(label="Name", max_length=30, required=True)
    email = forms.EmailField(label="Email", required=False)
