# Generated by Django 4.2.4 on 2023-10-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cart_size_orderplaced_size_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='size',
            field=models.PositiveIntegerField(default=1),
        ),
    ]