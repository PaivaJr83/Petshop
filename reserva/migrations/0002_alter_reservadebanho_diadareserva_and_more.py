# Generated by Django 4.2.4 on 2023-10-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservadebanho',
            name='diaDaReserva',
            field=models.DateField(verbose_name='Dia da Reserva'),
        ),
        migrations.AlterField(
            model_name='reservadebanho',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='reservadebanho',
            name='nomeDoPet',
            field=models.CharField(max_length=50, verbose_name='Nome do PET'),
        ),
        migrations.AlterField(
            model_name='reservadebanho',
            name='observacoes',
            field=models.TextField(blank=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='reservadebanho',
            name='tamanho',
            field=models.IntegerField(choices=[(0, 'Pequeno'), (1, 'Médio'), (2, 'Grande')], verbose_name='Tamanho'),
        ),
        migrations.AlterField(
            model_name='reservadebanho',
            name='telefone',
            field=models.CharField(max_length=15, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='reservadebanho',
            name='turno',
            field=models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde')], max_length=5, verbose_name='Turno'),
        ),
    ]
