# Generated by Django 4.1.6 on 2024-03-28 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_useremployeemodel_userstoremodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproductmodel',
            name='userstoreModel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_product', to='core.userstoremodel'),
        ),
    ]
