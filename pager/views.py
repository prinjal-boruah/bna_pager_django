from django.shortcuts import render
from . models import *
from gtts import gTTS
import time
from django.http import HttpResponse
import requests
from datetime import datetime
from pytz import timezone

def indexView(request):
    x = requests.get('http://106.51.15.203/api/api.php?action=LIST&type=PAGE')
    list_of_zones = x.json()
    context = {
        'audio_files' : SpeechData.objects.all(),
        'zones': list_of_zones,
    }
    return render(request, 'index.html', context)

def saveTextAudio(request):
    '''
    Function to save the generated text from speech and convert it to a audio file.
    postToDjango() function is used to send data to this function using ajax.
    '''

    received_text = request.GET.get("text", None)
    received_lang = request.GET.get("language", None)

    now_utc = datetime.now(timezone('UTC'))
    now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))

    date_now = now_asia.strftime("%d/%m/%Y")
    time_now = now_asia.strftime("%I:%M:%S %p")

    if received_text:
        if received_lang == "en-US":
            language = 'en'
        elif received_lang == "hi-EN":
            language = 'hi'

        current_time = str(round(time.time()))
        audio_save_location = "./media/audio/"+current_time+".mp3" #name of audio file
        audio_save_location_django = "audio/"+current_time+".mp3"
        myobj = gTTS(text=received_text, lang=language, slow=False)
        myobj.save(audio_save_location)
        savetext = SpeechData(text=received_text, manual_id=current_time, audioFile=audio_save_location_django, lang=language, date = date_now, time = time_now)
        savetext.save()
        return HttpResponse("Saved successfully")