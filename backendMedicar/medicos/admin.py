from django.contrib import admin
from backendMedicar.medicos.models import Medico

class MedicoAdmin(admin.ModelAdmin):
    fields = {'all'}

admin.site.register(Medico)

