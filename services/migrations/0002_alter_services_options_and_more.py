# Generated by Django 4.1.7 on 2023-03-08 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.RenameField(
            model_name='services',
            old_name='service_status',
            new_name='status',
        ),
    ]
