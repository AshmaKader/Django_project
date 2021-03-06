# Generated by Django 4.0.3 on 2022-03-21 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Sales Office-North India', 'Sales Office-North India'), ('Sales Office-South India', 'Sales Office-South India')], max_length=50)),
                ('role', models.CharField(choices=[('Sales Manager', 'Sales Manager'), ('Sales Team', 'Sales Team'), ('Sales Director', 'Sales Director')], max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
