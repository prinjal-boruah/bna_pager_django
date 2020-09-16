from django.db import models

class SpeechData(models.Model):
    lang = models.CharField(max_length=100)
    manual_id = models.IntegerField(unique=True, null=True, blank=True)
    text = models.TextField()
    audioFile = models.FileField(upload_to='audio/', null=True, blank=True)

    def __str__(self):
        return self.text
