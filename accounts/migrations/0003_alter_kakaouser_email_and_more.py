# Generated by Django 4.0.4 on 2022-07-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_kakaouser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakaouser',
            name='email',
            field=models.EmailField(blank=True, max_length=256, null=True, verbose_name='사용자이메일'),
        ),
        migrations.AlterField(
            model_name='kakaouser',
            name='profile_image_url',
            field=models.TextField(blank=True, null=True, verbose_name='썸네일 이미지 URL'),
        ),
        migrations.AlterField(
            model_name='kakaouser',
            name='thumbnail_image_url',
            field=models.TextField(blank=True, null=True, verbose_name='썸네일 이미지 URL'),
        ),
    ]