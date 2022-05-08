# Generated by Django 3.2.13 on 2022-05-04 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0004_auto_20220428_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Menu Item name')),
                ('name_en', models.CharField(max_length=250, null=True, verbose_name='Menu Item name')),
                ('name_ar', models.CharField(max_length=250, null=True, verbose_name='Menu Item name')),
                ('external_link', models.URLField(blank=True, null=True, verbose_name='External Url')),
                ('internal_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='+', to='wagtailcore.page', verbose_name='Page')),
            ],
        ),
    ]