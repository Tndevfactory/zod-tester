# Generated by Django 3.2.1 on 2022-07-17 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnammatriculecaisse',
            name='month',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
