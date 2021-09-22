from django import forms
from django.forms.widgets import Textarea

class EmailForm(forms.Form):
    full_name = forms.CharField(max_length=120)
    email = forms.EmailField(max_length=150)
    message = forms.CharField(widget=Textarea, max_length=1500)