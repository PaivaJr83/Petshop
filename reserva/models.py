from django.db import models

# Create your models here.
class ReservaDeBanho(models.Model):
  TAMANHO_OPCOES = (
    (0, 'Pequeno'),
    (1, 'Médio'),
    (2, 'Grande')
  )
  TURNO_OPCOES = (
    ('manha', 'Manhã'),
    ('tarde', 'Tarde')
  )
  nomeDoPet = models.CharField(verbose_name='Nome do PET', max_length=50)
  telefone = models.CharField(verbose_name='Telefone', max_length=15)
  email = models.EmailField(verbose_name='E-mail', max_length=75)
  diaDaReserva = models.DateField(verbose_name='Dia da Reserva')
  observacoes = models.TextField(verbose_name='Observações', blank=True)
  turno = models.CharField(verbose_name='Turno', choices=TURNO_OPCOES, max_length=5)
  tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
  petshop_id = models.ForeignKey(
    'Petshop',
     related_name='reservas',
     on_delete=models.CASCADE,
     blank=True,
     null=True,
     verbose_name='Unidade'
    )


  class Meta:
    verbose_name = 'Formulário de Reserva de Banho'
    verbose_name_plural = 'Formulários de Reservas de Banhos'
    ordering = ['id']

  def __str__(self):
    return f'Nome do Pet: {self.nomeDoPet} - Dia da Reserva: {self.diaDaReserva} - Turno: {self.turno}'


class Petshop(models.Model):
  nome = models.CharField(verbose_name='Petshop', max_length=50)
  rua = models.CharField(verbose_name='Endereco', max_length=100)
  numero = models.CharField(verbose_name='Numero', max_length=10)
  bairro = models.CharField(verbose_name='Bairro', max_length=50)

  class Meta:
    ordering = ['id']

  def __str__(self):
    return f'Petshop : {self.nome}'
  
  
  def qtd_reservas(self):
    return self.reservas.count()





