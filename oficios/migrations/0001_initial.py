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
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('ativo', models.BooleanField(default=True)),
                ('deputado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Deputado')),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='ContatoEntidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('telefone', models.CharField(blank=True, max_length=30, null=True)),
                ('fax', models.CharField(blank=True, max_length=30, null=True)),
                ('celular', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Contato de Pessoa ou Entidade',
                'verbose_name_plural': 'Contatos de Pessoa ou Entidade',
            },
        ),
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pronome', models.CharField(choices=[('À', 'À'), ('Ao', 'Ao')], help_text='Utilizado na emissão de documentos.', max_length=2)),
                ('tratamento', models.CharField(blank=True, help_text='Pronome de tratamento incluído nos documentos emitidos. Ex.: Vossa Excelência o Sr.', max_length=60, null=True)),
                ('nome', models.CharField(max_length=60)),
                ('logradouro', models.CharField(help_text='Nome da rua ou avenida.', max_length=100)),
                ('numero', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número')),
                ('bairro', models.CharField(max_length=60)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
                ('inicio_mandato', models.DateField(blank=True, null=True, verbose_name='Início do mandato')),
                ('fim_mandato', models.DateField(blank=True, null=True, verbose_name='Fim do mandato')),
                ('ativo', models.BooleanField(default=True)),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='oficios.Cargo')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Cidade')),
                ('deputado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Deputado')),
                ('partido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gabinete.Partido')),
                ('regional', models.ForeignKey(help_text='Regional a qual pertence a pessoa ou entidade.', on_delete=django.db.models.deletion.PROTECT, to='gabinete.Regional')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Pessoa ou Entidade',
                'verbose_name_plural': 'Pessoas ou Entidades',
            },
        ),
        migrations.CreateModel(
            name='EnvioOficio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enviado', models.BooleanField(default=False)),
                ('erros', models.TextField(blank=True, null=True)),
                ('data_hora_envio', models.DateTimeField(verbose_name='Data e hora de envio')),
            ],
            options={
                'verbose_name': 'Envio do Ofício',
                'verbose_name_plural': 'Envios dos Ofícios',
            },
        ),
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('assunto', models.CharField(max_length=100)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('deputado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Deputado')),
                ('regional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Regional')),
            ],
            options={
                'ordering': ('-data', 'assunto'),
                'verbose_name': 'Ofício',
                'verbose_name_plural': 'Ofícios',
            },
        ),
        migrations.AddField(
            model_name='enviooficio',
            name='oficio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficios.Oficio', verbose_name='Ofício'),
        ),
        migrations.AddField(
            model_name='contatoentidade',
            name='entidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oficios.Entidade'),
        ),
    ]
