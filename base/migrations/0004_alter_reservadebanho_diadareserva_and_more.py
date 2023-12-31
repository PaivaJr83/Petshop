# Generated by Django 4.2.4 on 2023-10-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_contato_options_contato_lido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservadebanho',
            name='diaDaReserva',
            field=models.DateField(verbose_name='Dia da Reserva'),
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
            name='telefone',
            field=models.CharField(max_length=15, verbose_name='Telefone'),
        ),
    ]
