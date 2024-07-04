from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Events, Prüflinge, AktuellePrüfungListe

class PrüflingeResource(resources.ModelResource):
    class Meta:
        model = Prüflinge
        exclude = ('id',)  # Exclude the ID field
        import_id_fields = ('fl',)  # Use 'fl' as the unique identifier for import

class PrüfungResource(resources.ModelResource):
    class Meta:
        model = AktuellePrüfungListe
        exclude = ('id',)  # Exclude the ID field
        import_id_fields = ('fl',)  # Use 'fl' as the unique identifier for import

class EventsResource(resources.ModelResource):
    class Meta:
        model = Events
        exclude = ('id',)  # Exclude the ID field
        import_id_fields = ('date',)  # Use a unique identifier field for import

@admin.register(Prüflinge)
class PrüflingeAdmin(ImportExportModelAdmin):
    resource_class = PrüflingeResource
    list_display = ('fl', 'name', 'bezahlt', 'prüfungsdatum')

@admin.register(AktuellePrüfungListe)
class AktuellePrüfungListeAdmin(ImportExportModelAdmin):
    resource_classes = [PrüfungResource]  # Ensure this is a list
    list_display = ('fl', 'name', 'prüfungsdatum', 'uhrzeit')

@admin.register(Events)
class EventsAdmin(ImportExportModelAdmin):
    resource_class = EventsResource
    list_display = ('date', 'text_event', 'uhrzeit')

