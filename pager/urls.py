from django.urls import path
from . import views

urlpatterns = [
    path('speechtext/', views.indexView),
    path('speechtext', views.indexView),
    path('', views.indexView),
    path('savetextaudio/', views.saveTextAudio),

    path('api/speechpost/', views.SpeechPostView.as_view({'get':'speechList'})),
    path('api/speechpost', views.SpeechPostView.as_view({'get':'speechList'})),
]
