from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Events, Prüflinge, AktuellePrüfungListe

class PrüflingeResource(resources.ModelResource):
    class Meta:
        model = Prüflinge
        fields = ('fl','name', 'bezahlt', 'prüfungsdatum')

@admin.register(Prüflinge)
class Foradmin(ImportExportModelAdmin):
    resource_class = PrüflingeResource
    list_display = ('fl' ,"name", "bezahlt", "prüfungsdatum")

admin.site.register(Events)

admin.site.register(AktuellePrüfungListe)
