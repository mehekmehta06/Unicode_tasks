# Generated by Django 4.2.4 on 2024-01-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_alter_userprofile_fname_alter_userprofile_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentmarketmodel',
            name='exchange',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='currentmarketmodel',
            name='symbol',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='currentmarketmodel',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='currentmarketmodel',
            name='stockname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
