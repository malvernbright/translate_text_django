from django.shortcuts import render
from django.http import HttpResponse
from translate import Translator

from . import forms


def index(request):
    return render(request, "translate_text/index.html")


def translation(request):
    if request.method == 'POST':
        form = forms.TranslateForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            translator = Translator(from_lang='english', to_lang='swahili')
            translation = translator.translate(input_text)
            # return HttpResponse(translation)
            context = {"translated": translation}
            return render(request, "translate_text/index.html", context)
        else:
            context = {"translated": "Could not send your request"}
            return render(request, "translate_text/index.html", context)
