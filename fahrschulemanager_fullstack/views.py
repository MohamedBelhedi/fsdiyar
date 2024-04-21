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
        redirect("/")  
   
    return render(request, 'loginregister.html')

def home(request):
    form = AnmeldeForms()
    pruefung = Events.objects.all()
    anzahl_prf = Events.objects.values_list("text_event", flat=True)
    print(anzahl_prf)
    for i in pruefung:
        print(i.date)
    prueflinge = Prüflinge.objects.all()
    prfl = []
    for i in prueflinge:
        prfl.append(i.name)
        print(prfl)
        print(len(prfl))

    if request.method =="POST":
        form = AnmeldeForms(request.POST)
        prfform = Pruefung(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            for i in anzahl_prf:
                Events.objects.filter(date = "2024-05-09").update(text_event = i - 1)
            # for i in pruefung:
            #     if "date" == i.date:
            #         Events.objects.filter(date = get date from prüfling).update(text_event = "1")

    if request.method == "POST" and 'logout' in request.POST:
        logout(request)
        render(request, 'loginregister.html')         
    context = {
        "pruefung": pruefung,
        "form": form
        }
    pruefung = Events.objects.all()
    return render(request, "home.html", context)