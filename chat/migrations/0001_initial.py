# Generated by Django 3.1.4 on 2020-12-09 19:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('users', models.ManyToManyField(blank=True, related_name='rooms_joined', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
