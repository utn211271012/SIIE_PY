# Generated by Django 4.0.4 on 2022-07-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEscolar', '0010_secatasignatura_seproasiindicador_seproplanestudio'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeCatDocumentacion',
            fields=[
                ('rowid_doc', models.IntegerField(primary_key=True, serialize=False)),
                ('id_doc', models.IntegerField()),
                ('descri_corto_doc', models.CharField(max_length=10)),
                ('descri_largo_doc', models.CharField(max_length=200)),
                ('importante_doc', models.CharField(max_length=1)),
                ('cve_control_doc', models.CharField(max_length=4)),
                ('estatus_grado', models.CharField(blank=True, max_length=15, null=True)),
                ('estatus_doc', models.CharField(blank=True, default='A', max_length=1, null=True)),
            ],
            options={
                'db_table': 'se_cat_documentacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeCatEstatusEstudiante',
            fields=[
                ('rowid_evento_est', models.IntegerField(primary_key=True, serialize=False)),
                ('id_evento_est', models.CharField(max_length=3)),
                ('consecutivo_est', models.IntegerField()),
                ('descri_largo_tipo_est', models.CharField(max_length=50)),
                ('descri_corto_tipo_est', models.CharField(max_length=10)),
                ('estatus_tipo_est', models.CharField(blank=True, default='A', max_length=1, null=True)),
            ],
            options={
                'db_table': 'se_cat_estatus_estudiante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeCatGrupo',
            fields=[
                ('rowid_grupo', models.IntegerField(primary_key=True, serialize=False)),
                ('id_grupo', models.IntegerField()),
                ('descri_largo_gpo', models.CharField(max_length=60)),
                ('descri_corto_gpo', models.CharField(max_length=10)),
                ('estatus_gpo', models.CharField(blank=True, max_length=1, null=True)),
                ('lim_gpo', models.IntegerField(blank=True, null=True)),
                ('lim_rec_gpo', models.IntegerField(blank=True, null=True)),
                ('lim_acu_gpo', models.IntegerField(blank=True, null=True)),
                ('lim_acu_rec_gpo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'se_cat_grupo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeTabEstudiante',
            fields=[
                ('rowid_matricula', models.IntegerField(primary_key=True, serialize=False)),
                ('id_matricula', models.FloatField()),
                ('nombre_estu', models.CharField(max_length=40)),
                ('paterno_est', models.CharField(max_length=30)),
                ('materno_est', models.CharField(max_length=30)),
                ('fec_nac_est', models.DateField()),
                ('entidad_nac', models.IntegerField(blank=True, null=True)),
                ('mpo_del_nac', models.IntegerField(blank=True, null=True)),
                ('estado_civil_est', models.CharField(blank=True, max_length=1, null=True)),
                ('trabaja_est', models.CharField(blank=True, max_length=1, null=True)),
                ('tel_trabajo', models.CharField(blank=True, max_length=15, null=True)),
                ('tipo_sangre_est', models.CharField(blank=True, max_length=10, null=True)),
                ('rfc_est', models.CharField(max_length=15)),
                ('curp_est', models.CharField(max_length=25)),
                ('direccion_est', models.CharField(max_length=60)),
                ('num_ext', models.CharField(blank=True, max_length=30, null=True)),
                ('num_int', models.CharField(blank=True, max_length=30, null=True)),
                ('codpos', models.CharField(max_length=5)),
                ('telefono_est', models.CharField(blank=True, max_length=15, null=True)),
                ('email_est', models.CharField(blank=True, max_length=50, null=True)),
                ('sexo_est', models.CharField(max_length=1)),
                ('edad_est', models.IntegerField(blank=True, null=True)),
                ('fecha_alta_est', models.DateField(blank=True, null=True)),
                ('user_alta_est', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_cambio_est', models.DateField(blank=True, null=True)),
                ('user_cambio_est', models.CharField(blank=True, max_length=10, null=True)),
                ('mat_tutor_est', models.CharField(blank=True, max_length=30, null=True)),
                ('pat_tutor_est', models.CharField(blank=True, max_length=30, null=True)),
                ('nombre_tutor_est', models.CharField(blank=True, max_length=40, null=True)),
                ('turno_est', models.IntegerField(blank=True, null=True)),
                ('generacion_est', models.IntegerField(blank=True, null=True)),
                ('periodo_est', models.IntegerField(blank=True, null=True)),
                ('anio_est', models.IntegerField(blank=True, null=True)),
                ('no_folio_est', models.IntegerField(blank=True, null=True)),
                ('id_tipo_esc_est', models.IntegerField(blank=True, null=True)),
                ('id_area_bach_est', models.IntegerField(blank=True, null=True)),
                ('entidad_bach', models.IntegerField(blank=True, null=True)),
                ('mpo_del_bach', models.IntegerField(blank=True, null=True)),
                ('fecha_ini_bach', models.IntegerField(blank=True, null=True)),
                ('fecha_fin_bach', models.IntegerField(blank=True, null=True)),
                ('promedio_gral_bach', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_vig_est', models.DateField(blank=True, null=True)),
                ('estatus_inscri_est', models.CharField(blank=True, max_length=1, null=True)),
                ('imss_est', models.CharField(blank=True, max_length=25, null=True)),
                ('clinica_est', models.IntegerField(blank=True, null=True)),
                ('num_servicio', models.FloatField(blank=True, null=True)),
                ('fec_ser_social', models.DateField(blank=True, null=True)),
                ('fecha_repos_est', models.DateField(blank=True, null=True)),
                ('matri_est', models.FloatField(blank=True, null=True)),
                ('beca_pro_est', models.CharField(blank=True, max_length=1, null=True)),
                ('usuario_est', models.CharField(blank=True, max_length=10, null=True)),
                ('password_est', models.CharField(blank=True, max_length=10, null=True)),
                ('estatus_biblio', models.CharField(blank=True, max_length=1, null=True)),
                ('tipo_carrera_est', models.IntegerField(blank=True, null=True)),
                ('otras_uts', models.IntegerField(blank=True, null=True)),
                ('no_cedula_tsu', models.CharField(blank=True, max_length=30, null=True)),
                ('no_referencia', models.CharField(blank=True, max_length=20, null=True)),
                ('grasc', models.CharField(blank=True, max_length=2, null=True)),
                ('institucion_seguro', models.CharField(blank=True, max_length=25, null=True)),
                ('otrainstitucionseguro', models.CharField(blank=True, max_length=40, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=20, null=True)),
                ('discapacidad', models.CharField(blank=True, max_length=5, null=True)),
                ('tipodiscapacidad', models.CharField(blank=True, max_length=40, null=True)),
                ('foliocertificado', models.CharField(blank=True, max_length=40, null=True)),
                ('fechaexpedicioncer', models.DateField(blank=True, null=True)),
                ('equivalencia', models.CharField(blank=True, max_length=5, null=True)),
                ('parentescotutor', models.CharField(blank=True, max_length=40, null=True)),
                ('tipoestudiante', models.CharField(blank=True, max_length=5, null=True)),
                ('estatus_est', models.CharField(blank=True, default='A', max_length=1, null=True)),
            ],
            options={
                'db_table': 'se_tab_estudiante',
                'managed': False,
            },
        ),
    ]
