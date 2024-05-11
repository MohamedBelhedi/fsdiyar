import datetime

from django.db import models
class Events(models.Model):
    date=models.DateField(blank=False, null=False)
    text_event=models.BigIntegerField(null=False, blank=False)
    def __str__(self):
        return "Prüfung am: "+ str(self.date)+", "+"Anzahl der Prüfung: "+str(self.text_event)

class Prüflinge(models.Model):
    name = models.CharField(null=True,max_length=255,blank=False)
    bezahlt = models.CharField(null=True,max_length=255,blank=False)
    prüfungsdatum = models.DateField(blank=False, null=False)

    def __str__(self):
        return "Name: "+str(self.name)+" "+"Bezahlt: "+str(self.bezahlt)+" "+"Prüfung am: "+str(self.prüfungsdatum)
