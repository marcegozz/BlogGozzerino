# Generated by Django 4.0.4 on 2022-07-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='etiqueta',
            field=models.CharField(default='Blogsito', max_length=255),
        ),
    ]