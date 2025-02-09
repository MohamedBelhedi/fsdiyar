from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import TüvTermine, Prüflinge, AktuellePrüfungListe, PrüflingeTheorie, BlockUnterricht, BlockUnterrichtSchueler

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

class TüvTermineResource(resources.ModelResource):
    class Meta:
        model = TüvTermine
        exclude = ('id',)  # Exclude the ID field
        import_id_fields = ('date',)  # Use a unique identifier field for import

class TheorieResource(resources.ModelResource):
    class meta:
        model = PrüflingeTheorie
        exclude = ('id',)
        import_id_fields = ('name',)

class SchuelerBlockUnterrichtResource(resources.ModelResource):
    class Meta:
        model = BlockUnterrichtSchueler
        exclude = ('id',)
        import_id_fields = ('name',)
class BlockUnterrichtResource(resources.ModelResource):
    class Meta:
        model = BlockUnterricht
        exclude = ('id',)
        import_id_fields = ('date', 'text_event', 'uhrzeit')
@admin.register(Prüflinge)
class PrüflingeAdmin(ImportExportModelAdmin):
    resource_class = PrüflingeResource
    list_display = ('fl', 'name', 'prüfungsdatum')

@admin.register(AktuellePrüfungListe)
class AktuellePrüfungListeAdmin(ImportExportModelAdmin):
    resource_classes = [PrüfungResource]  # Ensure this is a list
    list_display = ('fl', 'name', 'prüfungsdatum', 'uhrzeit')

@admin.register(TüvTermine)
class EventsAdmin(ImportExportModelAdmin):
    resource_class = TüvTermineResource
    list_display = ('date', 'text_event', 'uhrzeit')

@admin.register(PrüflingeTheorie)
class TheorieAdmin(ImportExportModelAdmin):
    resource_class = TheorieResource
    list_display = ('name', 'vorname', 'lernerfolg', 'anrufdatum')

@admin.register(BlockUnterricht)
class BlockUnterrichtResource(ImportExportModelAdmin):
    resource_class = BlockUnterrichtResource
    list_display = ('date', 'text_event', 'uhrzeit')


@admin.register(BlockUnterrichtSchueler)
class BlockUnterrichtSchuelerResource(ImportExportModelAdmin):
    resource_class = SchuelerBlockUnterrichtResource
    list_display = ('name', 'vorname', 'thema', 'datumthemaA', 'datumthemaB','datumthemaC', 'uhrzeitA', 'uhrzeitB', 'uhrzeitC')
