# Generated by Django 2.1.5 on 2020-02-18 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20200218_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='restaurants.Restaurant'),
        ),
    ]
