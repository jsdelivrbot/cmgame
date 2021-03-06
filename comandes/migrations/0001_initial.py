# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-15 13:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jocs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preu_total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('preuG_total', models.IntegerField(default=0)),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preuE', models.DecimalField(decimal_places=2, max_digits=7)),
                ('preuG', models.IntegerField()),
                ('data', models.DateField(auto_now=True)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comandes.Carret')),
                ('joc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joc_agafat', to='jocs.Joc')),
            ],
        ),
    ]
