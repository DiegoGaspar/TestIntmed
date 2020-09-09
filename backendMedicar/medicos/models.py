from django.db import models
from backendMedicar.especialidades.models import Especialidade

class Medico(models.Model):
    nome = models.CharField(max_length=250, null=False)
    crm = models.CharField(max_length=20, null=False)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome