# Generated by Django 4.0.5 on 2022-08-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_alter_actividad_options_alter_cursos_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='curso',
            field=models.CharField(max_length=100, verbose_name='Nombre del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='i',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Clave'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre completo'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='tiempo',
            field=models.TextField(max_length=100, verbose_name='Descripcion'),
        ),
    ]
