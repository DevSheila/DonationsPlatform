# Generated by Django 3.2.9 on 2022-02-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allusers',
            name='donee_category',
            field=models.CharField(choices=[('Childrens Home', 'Childrens Home'), ('Eldrey Shelter', 'Eldrey Shelter'), ('Street Families', 'Street Families')], max_length=50, null=True, verbose_name='Donee category'),
        ),
    ]