# Generated by Django 4.1.6 on 2024-03-25 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_userstoremodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProductModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id user product')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('UserstoreModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.userstoremodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
    ]