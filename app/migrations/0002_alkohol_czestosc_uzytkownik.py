# Generated by Django 2.1.7 on 2019-03-25 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alkohol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj_alkoholu', models.CharField(max_length=200)),
                ('piwo', models.CharField(max_length=100)),
                ('wodka', models.CharField(max_length=100)),
                ('wino', models.CharField(max_length=100)),
                ('inne', models.CharField(max_length=100)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Czestosc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('okazja', models.CharField(max_length=200)),
                ('czestotliwosc', models.CharField(max_length=200)),
                ('pierwszy_kontakt', models.CharField(max_length=100)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wiek', models.CharField(max_length=50)),
                ('plec', models.CharField(default='0', max_length=20)),
                ('miasto', models.CharField(max_length=100)),
                ('wyksztalcenie', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
            ],
        ),
    ]