# Generated by Django 2.1.15 on 2020-01-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200104_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='sub_position',
            field=models.CharField(max_length=1),
        ),
    ]
