from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .forms import AnmeldeForms, Pruefung
from .models import Events, Prüflinge, AktuellePrüfungListe
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index_view(request):
    if request.method == "POST" and "login" in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home/")
        else:
            return HttpResponse("<h1>Benutzer nicht gefunden oder Passwort falsch</h1> <a href=''>zurück</a>")

    if request.method == "POST" and 'logout' in request.POST:
        logout(request)
        return redirect("/")
    return render(request, 'loginregister.html')

@csrf_exempt
def home(request):
    form = Pruefung()
    prftexterr = ""
    aktuellePrüfung = AktuellePrüfungListe.objects.all()
    pruefung = Events.objects.all()
    anzahl_prf = Events.objects.all()
    prueflinge = Prüflinge.objects.all()
    prfl = [p.name for p in prueflinge]
    form = Pruefung(user=request.user)

    if request.method == "POST" and 'logout' in request.POST:
        logout(request)
        return redirect("/")

    if request.method == "POST":
        # form = Pruefung(request.POST)
        form = Pruefung(request.POST, user=request.user)
        date = request.POST.get('prüfungsdatum')
        prfname = request.POST.get('name')

        if prfname in prfl:
            return HttpResponse("<h1 style='text-align: center'>Der Name ist Doppelt drinne‼️ <a href=''>zurück zu Prüfungen</a></h1>")

        if form.is_valid():

            event_date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
            event = Events.objects.filter(date=event_date).first()

            if event:
                if event.text_event > 0:
                    event.text_event -= 1
                    event.save()

                    if prfname not in prfl:
                        form.save()
                        form._clean_form()

                    # Check if the event's text_event is now 0
                    if event.text_event == 0:
                        prftexterr = f"""Keine Prüfung Mehr für den {date} melde dich bitte im Büro"""
                else:
                    prftexterr = f"""Keine Prüfung Mehr für den {date} melde dich bitte im Büro"""
            else:
                prftexterr = f"""Keine Prüfung für das Datum {date} gefunden"""

    context = {
        "pruefung": pruefung,
        "form": form,
        "prftexterr": prftexterr,
    }
    return render(request, "home.html", context)
