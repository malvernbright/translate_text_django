import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from translate import Translator
from django.views.decorators.csrf import csrf_exempt

from . import forms


def index(request):
    return render(request, "translate_text/index.html")


@csrf_exempt
def translation(request):
    if request.method == 'POST':
        input_text = json.loads(request.body)
        translator = Translator(from_lang=input_text['from_lang'], to_lang=input_text['to_lang'])
        translation = translator.translate(input_text['input_text'])
        data = {"data": translation}
        return JsonResponse(data)
