from django.contrib import admin
from .models import Contract, AuditResult

# Register your models here.

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "client_name", "file", "completed", "created_at")
    list_filter = ("completed", "created_at")
    search_fields = ("client_name", "file")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


@admin.register(AuditResult)
class AuditResultAdmin(admin.ModelAdmin):
    list_display = ("id", "contract", "risk_level", "created_at")
    list_filter = ("risk_level", "created_at")
    search_fields = ("contract__client_name", "risk_level")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)