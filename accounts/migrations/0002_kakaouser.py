# Generated by Django 4.0.4 on 2022-07-27 18:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KakaoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256, verbose_name='사용자명')),
                ('email', models.EmailField(max_length=256, verbose_name='사용자이메일')),
                ('thumbnail_image_url', models.TextField(verbose_name='썸네일 이미지 URL')),
                ('profile_image_url', models.TextField(verbose_name='썸네일 이미지 URL')),
                ('connected_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
