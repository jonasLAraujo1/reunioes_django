# Generated by Django 2.2.7 on 2020-01-20 23:32

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('1', 'Novo'), ('2', 'Visualizado')], default='1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('inicio', models.TimeField()),
                ('fim', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Reuniao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pauta', models.CharField(max_length=120)),
                ('local', models.CharField(max_length=120)),
                ('semestre', models.CharField(max_length=6)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('deliberacoes', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('1', 'Agendada'), ('2', 'Confirmada'), ('3', 'Consolidada'), ('4', 'Cancelada')], default='1', max_length=1)),
                ('cor', models.CharField(choices=[('1', '#5C63DE'), ('2', '#CEC02D'), ('3', '#81CE2D'), ('4', '#2DCEB7')], default='1', max_length=1)),
                ('data_reuniao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Data')),
                ('tipo_reuniao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(blank=True, max_length=120, null=True)),
                ('funcao', models.CharField(blank=True, max_length=35, null=True)),
                ('cargo', models.CharField(blank=True, max_length=50, null=True)),
                ('lotacao', models.CharField(blank=True, max_length=35, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
