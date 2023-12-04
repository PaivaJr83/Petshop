import pytest
from rest_framework.test import APIClient
from datetime import date
from model_bakery import baker
from reserva.models import Petshop, ReservaDeBanho

@pytest.fixture
def dados_agendamento_valido():
    petshop = baker.make(Petshop)

    hoje = date.today()
    agendamento = {
        
        'nomeDoPet' : 'Leo',
        'email' : 'leo@gmail.com',
        'telefone' : '988027285',
        'diaDaReserva' : hoje,
        'turno' : 'manha',
        'tamanho' : 0,
        'petshop' : petshop.pk
    }
    return agendamento
@pytest.fixture
def agendamento():
    return baker.make(ReservaDeBanho)

@pytest.fixture
def usuario():
    return baker.make('auth.User')


@pytest.fixture
def dados_agendamento_isntancia():
    petshop = baker.make(Petshop)

    hoje = date.today()

    agendamento = {
        'nomeDoPet' : 'Leo',
        'email' : 'leo@gmail.com',
        'telefone' : '988027285',
        'diaDaReserva' : hoje,
        'turno' : 'manha',
        'tamanho' : 0,
        'petshop' : petshop
    }
    return agendamento


@pytest.mark.django_db
def test_listar_todos_petshops():
    client = APIClient()
    resposta = client.get('/api/petshop/')
    assert len(resposta.data['results']) == 0

@pytest.mark.django_db
def test_listar_todos_petshops_com_1_elemento(dados_agendamento_valido):
    client = APIClient()
    resposta = client.get('/api/petshop/')
    assert len(resposta.data['results']) == 1

@pytest.mark.django_db
def test_listar_todos_agendamentos():
    client = APIClient()
    resposta = client.get('/api/agendamento/')
    assert len(resposta.data['results']) == 1

@pytest.mark.django_db
def test_criar_agendamento(dados_agendamento_valido, usuario):
    client = APIClient
    client.force_authenticate(usuario)
    resposta = client.post('/api/agendamento/', dados_agendamento_valido)

    assert resposta.status_code == 201

@pytest.mark.django_db
def test_obter_agendamento_pelo_id(dados_agendamento_isntancia):
    ReservaDeBanho.objects.create(**dados_agendamento_isntancia)

    client = APIClient()
    resposta = client.get('/api/agendamento/1/')

  
    assert resposta.json()['nomeDoPet'] == 'Leo'
    assert resposta.json()['email'] == 'leo@gmail.com'

    assert resposta.status_code == 200


def test_deletar_agendamento(dados_agendamento_instancia,usuario):
    ReservaDeBanho.objects.create(**dados_agendamento_isntancia)

    client = APIClient()
    respostaPrimeiroGet = client.get('/api/agendamento/1/')

  
    assert respostaPrimeiroGet.json()['nomeDoPet'] == 'Leo'
    assert respostaPrimeiroGet.json()['email'] == 'leo@gmail.com'

    assert respostaPrimeiroGet.status_code == 200

    client.force_authenticate(usuario)
    client.delete('/api/agendamento/1')

    respostaSegundoGet = client.get('/api/agendamento/1')
    assert respostaSegundoGet.status_code == 404