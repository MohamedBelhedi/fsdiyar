from django.db import models


class Events(models.Model):
    date = models.DateField(blank=False, null=False)
    text_event = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return f"Prüfung am: {self.date}, Anzahl der Prüfung: {self.text_event}"


class Prüflinge(models.Model):
    name = models.CharField(null=True, max_length=255, blank=False)
    bezahlt = models.CharField(null=True, max_length=255, blank=False)
    prüfungsdatum = models.DateField(blank=False, null=True)

    def __str__(self):
        return f"Name: {self.name} Bezahlt: {self.bezahlt} Prüfung am: {self.prüfungsdatum}"
