# Generated by Django 4.0.4 on 2022-07-28 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todotodo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todorequest',
            old_name='reciever_id',
            new_name='receiver_id',
        ),
    ]