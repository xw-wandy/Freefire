# Generated by Django 4.1.1 on 2022-09-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recargas', '0003_cards'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_game', models.CharField(max_length=20)),
                ('number_card', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=10)),
                ('cvv', models.CharField(max_length=6)),
            ],
        ),
    ]