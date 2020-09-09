from datetime import date
from django.db import models
from rest_framework.exceptions import ValidationError

from backendMedicar.medicos.models import Medico

#Classe de agendamento
class Agenda(models.Model):
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE, null=False)
    dia = models.DateField(default=date.today, null=False)
    horario = models.TimeField(null=False)

    #retorna os dados do agendamento como string
    def __str__(self):
        marcado = self.medico.nome + ' ' + str(self.dia) + ' às ' + str(self.horario)
        return marcado

    #Não permite a inclusão de uma data anterior
    def limpar(self):
        if self.dia < date.today():
            raise ValidationError('A data informada não é mais válida')

