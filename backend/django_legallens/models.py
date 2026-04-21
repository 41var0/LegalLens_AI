from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Table "Contract"
class Contract(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="contracts/")
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.file.name} ({self.client_name}) - {"Completo" if self.completed else "Incompleto"}"

# Table "AuditResult"
class AuditResult(models.Model):
    RISK_LEVELS = [
        ("none", "Nada"),
        ("low", "Bajo"),
        ("medium", "Medio"),
        ("high", "Alto"),
    ]

    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    extracted_text = models.TextField()
    red_flags = models.TextField()
    risk_level = models.CharField(max_length=10, choices=RISK_LEVELS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resultado {self.contract.id} - {self.risk_level}"