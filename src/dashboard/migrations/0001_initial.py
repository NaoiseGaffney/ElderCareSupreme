# Generated by Django 3.0.8 on 2020-07-06 17:48

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60, null=True)),
                ('post_code', models.CharField(max_length=60, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('is_aider', models.BooleanField(default=False)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
