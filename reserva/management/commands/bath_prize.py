from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from reserva.models import Petshop, ReservaDeBanho


class Command(BaseCommand):
    help = 'Sortear uma quantidade escolhida de reservas de um petshop escolhido'

    def list_petshops_ids(self):
        return Petshop.objects.all().values_list('pk', flat=True)



    def add_arguments(self, parser):
        parser.add_argument(
        'quantity',
        nargs='?',
        default=5,
        type=int,
        help='Define a quantidade de reservas sorteadas' 
        )

        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.list_petshops_ids(),
            help='Define qual petshop deve ser feito o sorteio'
        )




    def handle(self, *args, **options):
       quantity = options['quantity']
       petshop_id = options['petshop']

       todas_reservas = ReservaDeBanho.objects.filter(petshop_id=petshop_id)

       for reserva in todas_reservas:
           self.stdout.write(str(reserva))