
from rest_framework import viewsets

from backendMedicar.agenda.models import Agenda
from backendMedicar.agenda.serializer import AgendaSerializer


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
