from django import forms
from django.views.decorators.csrf import csrf_protect

@csrf_protect
class TranslateForm(forms.Form):
    input_text = forms.CharField(label="Text to translate")