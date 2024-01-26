# Generated by Django 4.2.4 on 2024-01-18 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('Fname', models.CharField(default='', max_length=20)),
                ('Lname', models.CharField(default='', max_length=20)),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='username')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CurrentMarketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockname', models.CharField(max_length=20)),
                ('stockamt', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_id', models.IntegerField()),
                ('strat_time', models.DateField()),
                ('time_period', models.IntegerField(default=30)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResourcesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('article', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TransactionlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=3, max_length=10)),
                ('trans_id', models.IntegerField()),
                ('back_acc_no', models.IntegerField()),
                ('upi_id', models.EmailField(max_length=254)),
                ('mem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioapp.membershipmodel')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('contact_no', models.PositiveIntegerField()),
                ('stock_name', models.CharField(max_length=50)),
                ('stock_number', models.PositiveIntegerField()),
                ('stock_price', models.DecimalField(decimal_places=2, max_digits=3, max_length=15)),
                ('stock_date', models.DateField()),
                ('mf_name', models.CharField(max_length=50)),
                ('mf_amt', models.DecimalField(decimal_places=2, max_digits=3, max_length=20)),
                ('mf_date', models.DateField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roi', models.DecimalField(decimal_places=2, max_digits=3)),
                ('valuation', models.DecimalField(decimal_places=2, max_digits=3)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
