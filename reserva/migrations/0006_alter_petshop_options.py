# Generated by Django 4.2.4 on 2023-11-13 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0005_alter_reservadebanho_petshop_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petshop',
            options={'ordering': ['id']},
        ),
    ]