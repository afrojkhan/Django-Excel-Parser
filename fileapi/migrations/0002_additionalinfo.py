# Generated by Django 4.2.7 on 2023-12-23 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=100)),
                ('father_mobile', models.IntegerField()),
                ('father_age', models.IntegerField()),
                ('father_email', models.EmailField(max_length=100)),
            ],
        ),
    ]
