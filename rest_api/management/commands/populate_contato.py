from model_bakery import baker

from base.models import Contato

from django.core.management.base import BaseCommand

class Command(BaseCommand):
  help = 'Criar dados fakes para o nosso model de Contato'

  def handle(self, *args, **options):
    total = 100

    self.stdout.write(
      self.style.WARNING(f'Criando {total} contatos')
    )

    for i in range(total):
      self.stdout.write(
        self.style.WARNING(f'Criando contato número {i}')
      )
      reserva = baker.make(Contato)
      reserva.save()

    self.stdout.write(
      self.style.SUCCESS('Contatos criados com sucesso!!')
    )
