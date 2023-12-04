from pytest_django.asserts import assertTemplateUsed
import pytest
from datetime import date, timedelta
from reserva.models import ReservaDeBanho
from model_bakery import baker

def test_view_deve_retornar_template_correto(client):
    response = client.get('/reserva/criar/')

    assert response.status_code == 200

    assertTemplateUsed(response,'reserva_de_banho.html')

@pytest.fixture
def reserva_valida(client):
    data = date.today()
    reserva = {
        'nomeDoPet' : 'Leo',
        'email' : 'leo@gmail.com',
        'telefone' : '988027285',
        'diaDaReserva' : data,
        'turno' : 'manha',
        'tamanho' : 0,
    }
    return reserva

@pytest.fixture
def reserva_invalida(client):
    ontem = date.today() - timedelta(days=1)
    reserva = {
        'nomeDoPet' : 'Leo',
        'email' : 'leo@gmail.com',
        'telefone' : '988027285',
        'diaDaReserva' : ontem,
        'turno' : 'manha',
        'tamanho' : 0,
    }
    return reserva

@pytest.mark.django_db()
def test_view_deve_retornar_reserva_de_banho(client, reserva_valida):
    
    client.post('/reserva/criar/', reserva_valida)

    assert ReservaDeBanho.objects.all().count() == 1

    primeirareservaCriada = ReservaDeBanho.objects.first()

    assert primeirareservaCriada.nomeDoPet == reserva_valida['nomeDoPet']
    assert primeirareservaCriada.email == reserva_valida['email']
    assert primeirareservaCriada.turno == reserva_valida['turno']

@pytest.mark.django_db()
def test_view_deve_retornar_mensagem_de_sucesso(client, reserva_valida):
    response = client.post('/reserva/criar/', reserva_valida)

    assert response.status_code == 200

    assert 'Reserva feita com sucesso' in str(response.content)

@pytest.mark.django_db()
def test_view_deve_retornar_mensagem_de_erro_de_data_no_passado(client, reserva_invalida):
    response = client.post('/reserva/criar/', reserva_invalida)

    assert 'Não é possível reservar para uma data no passado.' in str(response.content)

@pytest.mark.django_db()
def test_view_deve_retornar_messagem_de_quantidade_limite_utrapassada(client, reserva_valida):
    quantidade = 4
    baker.make(
        ReservaDeBanho,
        quantidade,

    )
    response = client.post('/reserva/criar/', reserva_valida)

    assert 'O limite máximo de reservas para este dia já foi atingido. Escolha outra data.' in str(response.conte)