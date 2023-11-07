from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
  help = 'Criar um usuário e um token para ele'

  def add_arguments(self, parser):
    parser.add_argument('--username', required=True)
    parser.add_argument('--password', required=True)
    

  def handle(self, *args, **options):
    username = options['username']
    password = options['password']

    self.stdout.write(
      self.style.WARNING(f'Criando um usuário {username} com a senha {password}')
    )
    usuario = User(username=username)
    usuario.set_password(password)
    usuario.first_name = username
    usuario.save()

    self.stdout.write(
      self.style.SUCCESS('Usuário criando com sucesso!')
    )

    token = Token.objects.create(user=usuario)

    self.stdout.write(
    self.style.SUCCESS(f'Token gerado: {token}')
    )