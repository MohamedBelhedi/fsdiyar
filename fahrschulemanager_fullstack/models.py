from django.db import models

# Create your models here.
class Events(models.Model):
    date=models.DateField()
    text_event=models.BigIntegerField(null = False, blank = False)
    def __str__(self):
        return "Prüfung am: "+ str(self.date)+", "+"Anzahl der Prüfung: "+str(self.text_event)

class Prüflinge(models.Model):
    name = models.CharField(null=True,max_length=255,blank=False)
    bezahlt = models.CharField(null=True,max_length=255,blank=False)
    prüfungsdatum = models.DateField()

    def __str__(self):
        return "Name: "+self.name+" "+"Bezahlt: "+self.bezahlt+" "+"Prüfung am: "+str(self.prüfungsdatum)   
