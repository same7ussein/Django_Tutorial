# Generated by Django 4.0.6 on 2022-07-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_male'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='male',
            name='name_female',
        ),
        migrations.AddField(
            model_name='male',
            name='name_male',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='female',
            name='name_female',
            field=models.CharField(max_length=50, null=True),
        ),
    ]