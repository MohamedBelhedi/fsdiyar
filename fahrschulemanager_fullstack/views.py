import csv
from datetime import datetime
import datetime as dt
import pywhatkit

from django.db.models import Max
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout

from .forms import Pruefung, TheorieForm
from .models import TüvTermine, Prüflinge, AktuellePrüfungListe, PrüflingeTheorie
from django.views.decorators.csrf import csrf_exempt

date = dt.datetime.today().strftime('%Y-%m-%d')
datePrf = dt.datetime.today().strftime('%Y-%m-%d')
datePrfl = dt.datetime.today().strftime('%Y-%m-%d')


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
    prftexterr = ""
    pruefung = TüvTermine.objects.all()
    prueflinge = Prüflinge.objects.all()
    prfl = [p.name for p in prueflinge]
    form = Pruefung(user=request.user)
    if request.method == 'GET':
        for datum in pruefung:
            if datePrf > str(datum.date):
                pruefung.filter(date=str(datum.date)).delete()

        for datum in prueflinge:
            if datePrfl > str(datum.prüfungsdatum):
                prueflinge.filter(prüfungsdatum=str(datum.prüfungsdatum)).delete()

    if request.method == "POST" and 'logout' in request.POST:
        logout(request)
        return redirect("/")

    if request.method == "POST":
        pruefungTuev = TüvTermine.objects.all()
        form = Pruefung(request.POST, user=request.user)
        date = request.POST.get('prüfungsdatum')
        prfname = request.POST.get('name')

        if prfname in prfl:
            return HttpResponse(
                "<h1 style='text-align: center'>Der Name ist Doppelt drinne‼️ <a href=''>zurück zu Prüfungen</a></h1>")

        if form.is_valid():

            event_date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
            event = TüvTermine.objects.filter(date=event_date).first()

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
    if request.method == "POST" and "whatsapp" in request.POST:
        for items in pruefungTuev:
            print(items.date)
            pywhatkit.sendwhatmsg_to_group_instantly("KS1GVUvBxDKFvbm686Olvx",
                                                     f"Bitte einmal anmelden ueber die App (https://fsdiyar.onrender.com/) fuer den: {items.date.strftime("%d.%m.%Y")} {items.text_event} Pruefungen")
    context = {
        "pruefung": pruefung,
        "form": form,
        "prftexterr": prftexterr,
    }
    return render(request, "home.html", context)


@csrf_exempt
def theories(request):
    pruefungTheorie = PrüflingeTheorie.objects.all().order_by('anrufdatum', '-lernerfolg')
    theorieForm = TheorieForm()
    achtungText = ''
    highlighted_users = set()

    if request.method == "POST":
        if 'anmelden' in request.POST:
            theorieForm = TheorieForm(request.POST)
            lernerfolg = request.POST.get('lernerfolg')
            name = request.POST.get('name')
            vorname = request.POST.get('vorname')

            if theorieForm.is_valid():
                # Check for existing entry with the same name and vorname
                existing_entry = PrüflingeTheorie.objects.filter(name=name, vorname=vorname).first()
                if existing_entry:
                    achtungText = 'Schüler ist schon in der Liste'
                elif int(lernerfolg) > 79:
                    theorieForm.save()
                else:
                    achtungText = 'Der Schüler hat einen Lernerfolg unter 80 % Anmeldung nicht möglich'

        if 'lösche' in request.POST:
            delete_id = request.POST.get('delete_id')
            PrüflingeTheorie.objects.filter(id=delete_id).delete()

        if 'logout' in request.POST:
            logout(request)
            return redirect("/")

        if 'export' in request.POST:

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="pruefungen{dt.datetime.today().date()}.csv"'
            writer = csv.writer(response)
            writer.writerow(['Name', 'Vorname', 'Lernerfolg', 'Anrufdatum'])

            # Fetch the data from the database
            pruefungTheorie = PrüflingeTheorie.objects.all().order_by('anrufdatum', '-lernerfolg').values_list('name', 'vorname', 'lernerfolg', 'anrufdatum')

            for item in pruefungTheorie:
                writer.writerow(item)
            return response

    date_max_lernerfolg = pruefungTheorie.values('anrufdatum').annotate(max_lernerfolg=Max('lernerfolg'))
    for item in date_max_lernerfolg:
        highlighted_user = pruefungTheorie.filter(
            anrufdatum=item['anrufdatum'],
            lernerfolg=item['max_lernerfolg']
        ).first()
        if highlighted_user:
            highlighted_users.add(highlighted_user.id)

    # Assuming datePrf is defined somewhere in your code
    for datum in pruefungTheorie:
        if datePrf > str(datum.anrufdatum):
            PrüflingeTheorie.objects.filter(anrufdatum=datum.anrufdatum).delete()



    context = {
        "pruefungTheorie": pruefungTheorie,
        "theoieForm": theorieForm,
        "achtungText": achtungText,
        "highlighted_users": highlighted_users
    }

    return render(request, "theorie.html", context)

@csrf_exempt
def pruefung(request):
    prüfungen = AktuellePrüfungListe.objects.all()
    if request.method == "POST" and 'logout' in request.POST:
        logout(request)
        return redirect("/")
    if request.method == "GET":
        for datum in prüfungen:
            if date > str(datum.prüfungsdatum):
                prüfungen.filter(prüfungsdatum=str(datum.prüfungsdatum)).delete()
                print('test', datum.prüfungsdatum, date)


    context = {
        "prüfungen": prüfungen
    }

    return render(request, 'prüfungen.html', context)


