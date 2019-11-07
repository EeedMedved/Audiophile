# Generated by Django 2.2.7 on 2019-11-07 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingSystemVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dac',
            options={'verbose_name': 'ЦАП', 'verbose_name_plural': 'ЦАПы'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': 'Производитель', 'verbose_name_plural': 'Производители'},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефоны'},
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='have_minijack',
            new_name='has_minijack',
        ),
        migrations.AddField(
            model_name='phone',
            name='has_nfc',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='height',
            field=models.FloatField(default=0, verbose_name='Высота'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='presentation_year',
            field=models.PositiveSmallIntegerField(default=1970, verbose_name='Год начала продаж'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='ram',
            field=models.PositiveIntegerField(default=0, verbose_name='Объем ОЗУ в Мб'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='sim_card_number',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1, verbose_name='Количество сим-карт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='storage',
            field=models.PositiveIntegerField(default=0, verbose_name='Встроенная память в МБ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='thickness',
            field=models.FloatField(default=0, verbose_name='Толщина'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='width',
            field=models.FloatField(default=0, verbose_name='Ширина'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='dac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='phones.DAC'),
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название ОС')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Название версии ОС')),
                ('version', models.FloatField()),
                ('release_date', models.DateField(verbose_name='Дата релиза')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='phones.OperatingSystemVendor')),
            ],
        ),
        migrations.CreateModel(
            name='AudioCodec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='phones.Manufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='phone',
            name='official_os',
            field=models.ManyToManyField(to='phones.OperatingSystem'),
        ),
    ]