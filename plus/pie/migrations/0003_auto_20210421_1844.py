# Generated by Django 3.2 on 2021-04-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie', '0002_auto_20210421_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showchart',
            name='bucket',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='showchart',
            name='payment_mode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
