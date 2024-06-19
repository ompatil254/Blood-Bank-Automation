# Generated by Django 5.0.1 on 2024-04-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0003_rename_date_donationdrive_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='unit_status',
            field=models.CharField(choices=[('Donated', 'Donated'), ('Tested and Processed', 'Tested and Processed'), ('Available for Transfusion', 'Available for Transfusion'), ('Utilized', 'Utilized')], default='Donated', max_length=50),
        ),
    ]
