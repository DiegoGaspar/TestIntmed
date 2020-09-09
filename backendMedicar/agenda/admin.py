from django.contrib import admin
from backendMedicar.agenda.models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    fields = {'all'}

admin.site.register(Agenda)