from rest_framework import viewsets
from backendMedicar.medicos.models import Medico
from backendMedicar.medicos.serializer import MedicoSerializer


#TODO: definir create apenas para admin
class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
