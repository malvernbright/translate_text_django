from django.urls import path
from . import views

app_name = 'translate_text'
urlpatterns = [
    path('', views.index, name='index'),
    path('translate/', views.translation, name='translate')
]
