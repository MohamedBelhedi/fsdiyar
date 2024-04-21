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
    prueflinge = Prüflinge.objects.all()
    for i in prueflinge:
        print(len(i))

    if request.method =="POST":
        form = AnmeldeForms(request.POST)
        prfform = Pruefung(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            Events.objects.filter(text_event = "2").update(text_event = "1")
            
    if request.method == "POST" and 'logout' in request.POST:
        logout(request)
        render(request, 'loginregister.html')         
    context = {
        "pruefung": pruefung,
        "form": form
        }
    pruefung = Events.objects.all()
    return render(request, "home.html", context)