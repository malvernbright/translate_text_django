from django import forms

class TranslateForm(forms.Form):
    input_text = forms.CharField(label="Text to translate")