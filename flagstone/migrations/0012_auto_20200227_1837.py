# Generated by Django 3.0.2 on 2020-02-28 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0011_auto_20200227_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='praasa_march2020',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='praasa_march2020',
            name='last_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
