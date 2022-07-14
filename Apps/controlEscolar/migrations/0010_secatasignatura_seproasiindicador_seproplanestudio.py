# Generated by Django 4.0.4 on 2022-07-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEscolar', '0009_delete_accountsprofile_delete_authgroup_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeCatAsignatura',
            fields=[
                ('rowid_asignatura', models.IntegerField(primary_key=True, serialize=False)),
                ('id_asignatura', models.CharField(max_length=20)),
                ('descri_larga_asi', models.CharField(max_length=80)),
                ('descri_corto_asi', models.CharField(max_length=10)),
                ('estatus_asi', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'se_cat_asignatura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeProAsiIndicador',
            fields=[
                ('rowid_pro_asi_ind', models.IntegerField(primary_key=True, serialize=False)),
                ('porcentaje_pro_asi_idi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('comen_pro_asi_ind', models.CharField(blank=True, max_length=30, null=True)),
                ('estatus_peai', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'se_pro_asi_indicador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeProPlanEstudio',
            fields=[
                ('rowid_pro_plan_est', models.IntegerField(primary_key=True, serialize=False)),
                ('horas_plan_est', models.IntegerField()),
                ('creditos_plan_est', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nota_minima_apro_est', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_pon_final', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estatus_pea', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'se_pro_plan_estudio',
                'managed': False,
            },
        ),
    ]
