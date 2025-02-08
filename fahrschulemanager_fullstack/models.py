from django.db import models


class TüvTermine(models.Model):
    date = models.DateField(blank=False, null=False)
    text_event = models.BigIntegerField(null=False, blank=False)
    uhrzeit = models.TimeField(blank=False, null=True)

    def __str__(self):
        return f"Prüfung am und um : {self.date} {self.uhrzeit}, Anzahl der Prüfung: {self.text_event}"


class Prüflinge(models.Model):
    fl = models.CharField(blank=False, max_length=255)
    name = models.CharField(null=True, max_length=255, blank=False)
    prüfungsdatum = models.DateField(blank=False, null=True)

    def __str__(self):
        return f"Fahrlehrer: {self.fl} Name: {self.name} Prüfung am: {self.prüfungsdatum}"


class PrüflingeTheorie(models.Model):
    name = models.CharField(blank=False, max_length=255)
    vorname = models.CharField(blank=False, max_length=255)
    lernerfolg = models.BigIntegerField(blank=False, null=False)
    anrufdatum = models.DateField(blank=False, null=True)

    def __str__(self):
        return f"Name: {self.name} Vorname: {self.vorname} Lernerfolg: {self.lernerfolg}  Anrufdatum: {self.anrufdatum}"


class AktuellePrüfungListe(models.Model):
    fl = models.CharField(blank=False, max_length=255)
    name = models.CharField(null=True, max_length=255, blank=False)
    prüfungsdatum = models.DateField(blank=False, null=True)
    uhrzeit = models.TimeField(blank=False, null=True)

    def __str__(self):
        return f"Fahrlehrer: {self.fl} Name: {self.name}  Prüfung am: {self.prüfungsdatum} Uhrzeit: {self.uhrzeit}"


class BlockUnterricht(models.Model):
    date = models.DateField(blank=False, null=False)
    text_event = models.TextField(null=False, blank=False)
    uhrzeit = models.TimeField(blank=False, null=True)

    def __str__(self):
        return f"Block Unterricht : {self.date} {self.uhrzeit}, Thema: {self.text_event}"


class BlockUnterrichtSchueler(models.Model):
    name = models.CharField(blank=False, max_length=255)
    vorname = models.CharField(blank=False, max_length=255)
    thema = models.CharField(blank=False, max_length=255)
    datum = models.DateField(blank=False, null=False)
    uhrzeit = models.TimeField(blank=False, null=True)
    def __str__(self):
        return f"Schüler Liste Block Unterricht : {self.name} {self.vorname}, Thema: {self.thema}, Datum: {self.datum}, Uhrzeit: {self.uhrzeit}"
