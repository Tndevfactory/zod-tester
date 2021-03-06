# Generated by Django 3.2.1 on 2022-07-18 09:16

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
            name='Releve',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rownum', models.CharField(blank=True, max_length=6, null=True)),
                ('matricule', models.CharField(blank=True, max_length=50, null=True)),
                ('cle', models.CharField(blank=True, max_length=8, null=True)),
                ('annee', models.CharField(blank=True, max_length=18, null=True)),
                ('salaire', models.CharField(blank=True, max_length=98, null=True)),
                ('classe', models.CharField(blank=True, max_length=98, null=True)),
                ('assure', models.JSONField(blank=True, null=True)),
                ('employeur', models.JSONField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
