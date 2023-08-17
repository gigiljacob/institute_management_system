from django.contrib import admin

from institutes.models import Institute


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    fields = ('identifier', 'name', 'type', 'address', 'phone', 'mobile', 'email', 'objective', 'bord', 'ownership', 'documents',
              'tan', 'license', 'accreditation', 'approvals', 'declaration')
    list_display = ('name', 'mobile', 'email', 'created_by', 'created_at', 'updated_by', 'updated_at')
    exclude = ('created_by', 'updated_by')
