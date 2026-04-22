from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ["user", "file", "client_name", "completed"]
        widgets = {
            "client_name": forms.TextInput(attrs={"class": "form-control"}),
            "file": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_client_name(self):
        name = self.cleaned_data.get("client_name")
        if not name:
            raise forms.ValidationError("El nombre del cliente es obligatorio.")
        return name