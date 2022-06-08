# Generated by Django 4.0.3 on 2022-03-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_remove_employee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user_name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(max_length=50),
        ),
    ]
