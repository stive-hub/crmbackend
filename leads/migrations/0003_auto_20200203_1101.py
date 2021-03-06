# Generated by Django 3.0.2 on 2020-02-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20200131_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='form_submission_time',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='form_type',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='industry',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='loc_of_hire',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
