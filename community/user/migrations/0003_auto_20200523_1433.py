# Generated by Django 3.0.6 on 2020-05-23 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200523_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user_info',
        ),
    ]
