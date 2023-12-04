import pytest
from datetime import date, timedelta
from model_bakery import baker
from rest_api.serializers import AgendamentoModelSerializer
from reserva.models import Petshop


@pytest.mark.django_db
def agendamento_com_data_no_passado():
    petshop = baker.make(Petshop)
    ontem = date.today() - timedelta(days=1)

    agendamento = {
        
        'nomeDoPet' : 'Pipoca',
        'email' : 'pipoca@gmail.com',
        'telefone' : '988027285',
        'diaDaReserva' : ontem,
        'turno' : 'manha',
        'tamanho' : 0,
        'petshop' : petshop.pk
    }
    return agendamento

@pytest.mark.django_db
def test_data_invalida_agendamento(agendamento_com_data_no_passado):
    serializer = AgendamentoModelSerializer(data=agendamento_com_data_no_passado)

    assert not serializer.is_valid()
