# Generated by Django 2.2.7 on 2020-03-07 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user_servidor'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerta',
            name='acao',
            field=models.CharField(default='informacao/3', max_length=120),
        ),
    ]