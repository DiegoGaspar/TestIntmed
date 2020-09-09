from rest_framework import serializers

from backendMedicar.agenda.models import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'