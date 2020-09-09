from rest_framework import viewsets

from backendMedicar.especialidades.models import Especialidade
from backendMedicar.especialidades.serializer import EspecialidadeSerializer


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
