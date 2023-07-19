from django.contrib import admin
from .models import Document
# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'file', 'file_format', 'created_at']
    list_filter = ['owner','file_format', 'created_at']