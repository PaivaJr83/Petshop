from reserva.models import ReservaDeBanho, Petshop
from model_bakery import baker
import pytest
from datetime import date

def test_basico():
    assert 1==1

@pytest.fixture
def reserva():
    data = date(2023, 10, 23)
    reserva = baker.make(
        ReservaDeBanho,
        nomeDoPet = 'Beck',
        turno = 'manha',
        diaDaReserva = data
    )
    return reserva

@pytest.mark.django_db()
def test_reserva_de_banho_deve_retornar_a_string_formatada(reserva):
  
    assert str(reserva) == 'Nome do Pet: Beck - Dia da Reserva: 2023-10-23 - Turno: manha'

@pytest.mark.django_db()
def test_deve_retornar_a_qtd_de_reservas_correta():
    petshop =  baker.make(Petshop)
    quantidade = 3

    baker.make(
        ReservaDeBanho,
        quantidade,
        petshop_id = petshop
    )
    assert petshop.qtd_reservas() == 3
  
