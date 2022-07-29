# Generated by Django 4.0.4 on 2022-07-29 14:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('color', models.CharField(default='#DDDDDD', max_length=7)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('emoji', models.TextField(default='', max_length=256)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(default=dict, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todotodo.category')),
                ('sender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TodoRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=256)),
                ('todo_start_date', models.DateField(default=django.utils.timezone.now)),
                ('todo_end_date', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('message', models.TextField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiver_persona', models.ForeignKey(default=dict, on_delete=django.db.models.deletion.CASCADE, related_name='todo_receiver_persona', to='todotodo.persona')),
                ('sender', models.ForeignKey(default=dict, on_delete=django.db.models.deletion.CASCADE, related_name='todo_sender', to=settings.AUTH_USER_MODEL)),
                ('todo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todotodo.todo')),
            ],
        ),
        migrations.CreateModel(
            name='PersonaPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('friendship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.friendship')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todotodo.persona')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todotodo.persona'),
        ),
    ]
