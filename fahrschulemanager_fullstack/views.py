from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from .forms import AnmeldeForms, Pruefung
from .models import Events, Prüflinge


def index_view(request):
    text = ''
    if request.method == "POST" and "login" in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username , password=password) 
        if user is not None:
            login(request,user)
            # return render(request, "home.html")
            return redirect("home/")
            
        else:
            return HttpResponse("<h1>Benutzer nicht gefunden oder Passwort falsch</h1> <a href=''>zurück</a>")
    if request.method == "POST" and 'logout' in request.POST:
        logout(request)
        return redirect("/")
   
    return render(request, 'loginregister.html')

def home(request):
    form = Pruefung()
    pruefung = Events.objects.all()
    anzahl_prf = Events.objects.values_list("text_event", flat=True)
    prueflinge = Prüflinge.objects.all()
    prfl = []
    for i in prueflinge:
        prfl.append(i.name)
    if request.method == "POST" and 'logout' in request.POST:
        logout(request)
        return redirect("/")

    if request.method == "POST":
        form = Pruefung(request.POST)
        date = request.POST.get('prüfungsdatum')
        prfname = request.POST.get('name')
        for i in anzahl_prf:
            if i == 0:
                Events.objects.filter(date=datetime.strptime(date, "%d.%m.%Y").strftime("%Y-%m-%d")).update(
                    text_event=0)
                return HttpResponse(f"""
                         <h1> Keine Prüfung Mehr für den {date} melde dich bitte im Büro</h1>
                         <a href="/home"> Zurück Zur Prüfanmeldung</a>
                         """)
        if prfname in prfl:
            print(" ja keine Doppelnamen  Bitte")
            return HttpResponse("<h1>Der Name ist Doppelt drinne</h1> <a href"">zurück</a>")

        elif form.is_valid():
            request.POST.get('name')
            request.POST.get('bezahlt')
            request.POST.get('prüfungsdatum')
            form.save()
            form.cleaned_data

            for i in anzahl_prf:
                Events.objects.filter(date = datetime.strptime(date, "%d.%m.%Y").strftime("%Y-%m-%d")).update(text_event = i - 1)

    if request.method == "POST" and 'logout' in request.POST:
        logout(request)
        render(request, 'loginregister.html')
    context = {
        "pruefung": pruefung,
        "form": form
        }
    return render(request, "home.html", context)