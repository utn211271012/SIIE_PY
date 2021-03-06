# Generated by Django 4.0.3 on 2022-07-29 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEscolar', '0011_secatdocumentacion_secatestatusestudiante_secatgrupo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeCatAsentamiento',
            fields=[
                ('rowid_asentamiento', models.AutoField(primary_key=True, serialize=False)),
                ('id_asentamiento', models.IntegerField()),
                ('descri_largo_asentamiento', models.CharField(max_length=50)),
                ('descri_corto_asentamiento', models.CharField(max_length=10)),
                ('estatus_asentamiento', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'se_cat_asentamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeCatEscuelaProcedencia',
            fields=[
                ('rowid_esc_proc', models.AutoField(primary_key=True, serialize=False)),
                ('cct_esc_proc', models.CharField(max_length=20)),
                ('nombre_esc_proc', models.CharField(max_length=200)),
                ('control_esc_proc', models.CharField(max_length=20)),
                ('servicio_esc_proc', models.CharField(blank=True, max_length=50, null=True)),
                ('estatus_esc_proc', models.CharField(blank=True, default='A', max_length=1, null=True)),
            ],
            options={
                'db_table': 'se_cat_escuela_procedencia',
                'managed': False,
            },
        ),
    ]
