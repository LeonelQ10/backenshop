# Generated by Django 4.1.6 on 2024-03-21 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShopModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id user shop')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Usuario Tienda',
                'verbose_name_plural': 'Usuarios Tienda',
                'db_table': 'user_shop',
            },
        ),
    ]
