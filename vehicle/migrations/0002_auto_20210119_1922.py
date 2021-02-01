# Generated by Django 3.0.8 on 2021-01-19 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stolenvehicle',
            name='make_name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='MakeModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('make_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleMakes')),
            ],
        ),
    ]
