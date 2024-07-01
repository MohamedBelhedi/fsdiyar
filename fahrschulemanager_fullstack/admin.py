from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Events, Prüflinge

class PrüflingeResource(resources.ModelResource):
    class Meta:
        model = Prüflinge
        fields = ('name', 'bezahlt', 'prüfungsdatum')

@admin.register(Prüflinge)
class Foradmin(ImportExportModelAdmin):
    resource_class = PrüflingeResource
    list_display = ("name", "bezahlt", "prüfungsdatum")

admin.site.register(Events)