# Generated by Django 3.2.13 on 2022-05-31 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.CharField(choices=[('a', 'advertisement'), ('b', 'investing'), ('c', 'Staying in touch')], max_length=50, verbose_name='Interests')),
                ('is_publisher', models.BooleanField(default=False, verbose_name='Publisher')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to=settings.AUTH_USER_MODEL, unique=True, verbose_name='User')),
            ],
        ),
    ]