from django.contrib import admin
from backendMedicar.especialidades.models import Especialidade

class EspecialidadeAdmin(admin.ModelAdmin):
    fields = {'all'}

admin.site.register(Especialidade)