from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from user.models import Profile


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('user', 'total_pontos',)
