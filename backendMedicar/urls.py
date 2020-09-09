from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backendMedicar.agenda.views import AgendaViewSet
from backendMedicar.especialidades.views import EspecialidadeViewSet
from backendMedicar.medicos.views import MedicoViewSet

router = routers.DefaultRouter()
router.register(r'Especialidades', EspecialidadeViewSet)
router.register(r'Agenda', AgendaViewSet)
router.register(r'Medico', MedicoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
