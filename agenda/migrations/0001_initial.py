# Generated by Django 2.0.6 on 2018-06-16 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gabinete', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companhia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Companhia aérea',
                'verbose_name_plural': 'Companhias aéreas',
            },
        ),
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_inicio', models.DateTimeField(verbose_name='Data e Hora de início')),
                ('data_hora_fim', models.DateTimeField(verbose_name='Data e Hora de término')),
                ('local', models.CharField(help_text='Local do evento', max_length=60)),
                ('descricao', models.TextField(help_text='Descrição geral do evento, para que o parlamentar saiba do que se trata.', verbose_name='Descrição')),
                ('obs', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Cidade')),
                ('deputado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Deputado')),
            ],
            options={
                'ordering': ('data_hora_inicio',),
            },
        ),
        migrations.CreateModel(
            name='TipoCompromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('ativo', models.BooleanField(default=True)),
                ('deputado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Deputado')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Tipo de compromisso',
                'verbose_name_plural': 'Tipos de compromisso',
            },
        ),
        migrations.CreateModel(
            name='Voo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_partida', models.DateTimeField(verbose_name='Data e horário de partida')),
                ('data_hora_chegada', models.DateTimeField(verbose_name='Data e horário de chegada')),
                ('localizador', models.CharField(help_text='Código localizador do vôo.', max_length=60)),
                ('numero', models.CharField(help_text='Número do vôo', max_length=20)),
                ('portao', models.CharField(max_length=30, verbose_name='Portão de embarque')),
                ('assento', models.CharField(help_text='Número do assento', max_length=20)),
                ('obs', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('cidade_chegada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cidade_chegada_voo', to='gabinete.Cidade', verbose_name='Cidade de chegada')),
                ('cidade_partida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cidade_partida_voo', to='gabinete.Cidade', verbose_name='Cidade de partida')),
                ('companhia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.Companhia', verbose_name='Companhia aérea')),
                ('deputado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Deputado')),
            ],
            options={
                'ordering': ('data_hora_partida',),
                'verbose_name': 'Vôo',
                'verbose_name_plural': 'Vôos',
            },
        ),
        migrations.AddField(
            model_name='compromisso',
            name='tipo',
            field=models.ForeignKey(help_text='Define o tipo de compromisso do parlamentar. Ex.: Reunião, Evento festivo, Etc.', on_delete=django.db.models.deletion.PROTECT, to='agenda.TipoCompromisso'),
        ),
    ]
