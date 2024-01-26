# Generated by Django 4.2.4 on 2024-01-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0009_alter_transactionlogmodel_trans_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentmodel',
            name='roi',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='investmentmodel',
            name='valuation',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='mf_amt',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='stock_number',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='stock_price',
            field=models.IntegerField(max_length=15),
        ),
    ]
