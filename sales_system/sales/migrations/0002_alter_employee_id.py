# Generated by Django 4.0.3 on 2022-03-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]