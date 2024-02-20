# Generated by Django 5.0.2 on 2024-02-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_load', models.FileField(upload_to='documents/', verbose_name='Файл')),
                ('check_file', models.BooleanField(default=False, verbose_name='Файл принят')),
                ('checkout_file', models.BooleanField(default=False, verbose_name='Файл Отклонен')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]
