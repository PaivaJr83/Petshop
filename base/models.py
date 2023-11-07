from django.db import models

class Contato(models.Model):
  nome = models.CharField(max_length=50)
  email = models.EmailField(max_length=75)
  mensagem = models.TextField()
  data = models.DateTimeField(auto_now_add=True)
  lido = models.BooleanField(default=False, blank=True)

  def __str__(self):
    return f'Nome: {self.nome} - Email: {self.email}'
  class Meta:
    verbose_name = 'Formulário de Contato'
    verbose_name_plural = 'Formulários de Contatos'
    ordering = ['-nome']


class ReservaDeBanho(models.Model):
  nomeDoPet = models.CharField(verbose_name='Nome do PET', max_length=50)
  telefone = models.CharField(verbose_name='Telefone', max_length=15)
  diaDaReserva = models.DateField(verbose_name='Dia da Reserva')
  observacoes = models.TextField(verbose_name='Observações', blank=True)