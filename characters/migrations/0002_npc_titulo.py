# Generated by Django 3.1.4 on 2021-02-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='npc',
            name='titulo',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
