from django.urls import path
from . import views

urlpatterns = [
    path('speechtext/', views.indexView),
    path('savetextaudio/', views.saveTextAudio)
]
