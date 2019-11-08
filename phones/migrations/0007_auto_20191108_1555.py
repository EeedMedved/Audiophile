# Generated by Django 2.2.7 on 2019-11-08 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_phone_display_resolution'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayTechnology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Технология изготовления')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='quick_charge_technology',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='display_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='phones.DisplayTechnology'),
        ),
    ]