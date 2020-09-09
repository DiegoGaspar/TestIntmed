from rest_framework import serializers

from backendMedicar.medicos.models import Medico
from backendMedicar.especialidades.serializer import EspecialidadeSerializer


class MedicoSerializer(serializers.ModelSerializer):

    especialidade = EspecialidadeSerializer()

    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'especialidade']
