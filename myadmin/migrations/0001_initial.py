# Generated by Django 3.2.1 on 2022-07-22 10:16

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
            name='Usermanage',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('authorities', models.JSONField(blank=True, null=True)),
                ('activated', models.CharField(blank=True, max_length=200, null=True)),
                ('login', models.CharField(blank=True, max_length=160, null=True)),
                ('firstName', models.CharField(blank=True, max_length=200, null=True)),
                ('lastName', models.CharField(blank=True, max_length=200, null=True)),
                ('manisupality', models.CharField(blank=True, max_length=200, null=True)),
                ('imageUrl', models.CharField(blank=True, max_length=200, null=True)),
                ('langKey', models.CharField(blank=True, max_length=200, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('createdDate', models.CharField(blank=True, max_length=200, null=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=200, null=True)),
                ('lastModifiedDate', models.CharField(blank=True, max_length=200, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
