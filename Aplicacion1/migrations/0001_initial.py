# Generated by Django 4.1 on 2023-02-07 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso1',
            fields=[
                ('codigo1', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nombre1', models.CharField(max_length=50)),
                ('creditos1', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso2',
            fields=[
                ('codigo2', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nombre2', models.CharField(max_length=50)),
                ('creditos2', models.PositiveBigIntegerField()),
            ],
        ),
    ]
