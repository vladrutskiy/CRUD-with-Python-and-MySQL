# Generated by Django 5.1.6 on 2025-02-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_salespersons_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TrackId', models.SmallIntegerField(max_length=10)),
                ('Name', models.CharField(max_length=24)),
                ('AlbumId', models.SmallIntegerField(max_length=10)),
                ('MediaTypeId', models.SmallIntegerField(max_length=10)),
                ('GenreId', models.SmallIntegerField(max_length=10)),
                ('Composer', models.CharField(max_length=35)),
                ('Milliseconds', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'Track',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='salespersons',
            table='SalesPersons',
        ),
    ]
