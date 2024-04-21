from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Events, Prüflinge


# Register your models here.
admin.site.register(Events)
@admin.register(Prüflinge)
class Foradmin(ImportExportModelAdmin):
    list_display=("name","bezahlt","prüfungsdatum")
    pass