from django.urls import path

from rest_framework.routers import SimpleRouter

from rest_api.views import *

app_name = 'rest_api'

router = SimpleRouter()
router.register('agendamento', AgendamentoModelViewSet)
router.register('contato', ContatoModelViewSet)


urlpatterns = [
  path('hello_world', hello_world, name='hello_world_api'),
  path('contato-inicial', listar_contatos, name='listar_contatos'),
  path('contato-inicial/<int:id>', obter_contato_pelo_id, name="obter_contato"),
]

urlpatterns += router.urls

