# Generated by Django 2.0.5 on 2018-05-23 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Deputado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Gênero')),
                ('tratamento', models.CharField(blank=True, max_length=60, null=True)),
                ('nome', models.CharField(max_length=60)),
                ('mensagem', models.CharField(blank=True, max_length=60, null=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoDeputado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('bairro', models.CharField(max_length=60)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
                ('telefone', models.CharField(blank=True, max_length=30, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Cidade')),
                ('deputado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Deputado')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('sigla', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('sigla', models.CharField(max_length=30)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('ativa', models.BooleanField(default=True)),
                ('deputado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Deputado')),
            ],
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Pais'),
        ),
        migrations.AddField(
            model_name='deputado',
            name='partido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Partido'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gabinete.Estado'),
        ),
    ]
