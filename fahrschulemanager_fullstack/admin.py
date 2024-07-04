# from django.contrib import admin
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
# from .models import Events, Prüflinge, AktuellePrüfungListe
#
# class PrüflingeResource(resources.ModelResource):
#     class Meta:
#         model = Prüflinge
#         fields = ('fl', 'name', 'bezahlt', 'prüfungsdatum')
#         exclude = ('id',)
#
# class PrüfungResource(resources.ModelResource):
#     class Meta:
#         model = AktuellePrüfungListe
#         fields = ('fl', 'name', 'prüfungsdatum', 'uhrzeit')
#         exclude = ('id',)
#
# @admin.register(Prüflinge)
# class PrüflingeAdmin(ImportExportModelAdmin):
#     resource_class = PrüflingeResource
#     list_display = ('fl', 'name', 'bezahlt', 'prüfungsdatum')
#     exclude = ('id',)
#
# @admin.register(AktuellePrüfungListe)
# class AktuellePrüfungListeAdmin(ImportExportModelAdmin):
#     resource_classes = [PrüfungResource]
#     list_display = ('fl', 'name', 'prüfungsdatum', 'uhrzeit')
#     exclude = ('id',)
#
# admin.site.register(Events)

from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
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

@admin.register(Prüflinge)
class PrüflingeAdmin(ImportExportModelAdmin):
    resource_class = PrüflingeResource
    list_display = ('fl', 'name', 'bezahlt', 'prüfungsdatum')

@admin.register(AktuellePrüfungListe)
class AktuellePrüfungListeAdmin(ImportExportModelAdmin):
    resource_classes = [PrüfungResource]  # Ensure this is a list
    list_display = ('fl', 'name', 'prüfungsdatum', 'uhrzeit')

admin.site.register(Events)

