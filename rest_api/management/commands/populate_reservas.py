from model_bakery import baker

from base.models import ReservaDeBanho

from django.core.management.base import BaseCommand

class Command(BaseCommand):
  help = 'Criar dados fakes para o nosso model de Reserva de Banho'

  def handle(self, *args, **options):
    total = 100

    self.stdout.write(
      self.style.WARNING(f'Criando {total} reservas')
    )

    for i in range(total):
      self.stdout.write(
        self.style.WARNING(f'Criando reserva número {i}')
      )
      reserva = baker.make(ReservaDeBanho)
      reserva.save()

    self.stdout.write(
      self.style.SUCCESS('Reservas criadas com sucesso!!')
    )
