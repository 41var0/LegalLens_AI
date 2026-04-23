from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Contract, AuditResult
import requests


FASTAPI_URL = "http://ai-engine:8000/upload"

class HomeDashboard(ListView):

    model = Contract
    template_name = 'HomeDashboard.html'


    def get_documentos_by_lawyer(self):
        lawyer_id = self.request.user.id
        docs = Contract.objects.all().filter(lawyer=lawyer_id).order_by('created_at')
        return docs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["documentos_legales"] = self.get_documentos_by_lawyer()

        return context





#########################################################################################
#########################################################################################

def subir_documento(request):

    if (request.method == "POST"):

        contract = Contract.objects.create(
            file=request.FILES["doc"],
            lawyer=User.objects.get(id=request.POST.get("lawyer_id")),
            client_name=request.POST.get("clientename"),
        )

        contract.save()

        return redirect("dashboard")

    return redirect("dashboard")




def realizar_auditacion(request):

    if (request.method == "POST"):

        doc = Contract.objects.get(id=request.POST.get("doc_id")) # FIXME NO IMLPEMENTADO DEL TODO

        nueva_auditacion = AuditResult.objects.create(
            contract=doc
        )


        # Obtenemos lso resultados de la IA
        result = __send_pdf_to_ai(file_path=doc.file)

        # Guardar todo
        nueva_auditacion.extracted_text = result.get("extracted_text", "")
        nueva_auditacion.red_flags = result.get("red_flags", "")
        nueva_auditacion.risk_level = result.get("risk_level", "None")
        nueva_auditacion.save()

        doc.completed = True
        doc.save()

        return redirect("dashboard")


    return redirect("dashboard")



def __send_pdf_to_ai(file_path:str) -> dict:
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(FASTAPI_URL, files=files)
    if response.status_code != 200:
        raise Exception(f"Error comunicando con AI Engine ({response.status_code})")

    return response.json()



