# Generated by Django 2.1.2 on 2018-10-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0009_auto_20181011_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xactno', models.CharField(max_length=200)),
                ('pltno', models.CharField(default='m', max_length=100)),
                ('car_tp', models.CharField(max_length=100)),
                ('vil_dt', models.CharField(max_length=100)),
                ('vil_tm', models.EmailField(blank=True, default='', max_length=100)),
                ('vil_add', models.CharField(blank=True, default='', max_length=200)),
                ('rule_1', models.TextField()),
                ('vildatetime', models.DateTimeField(auto_now=True)),
                ('vilinf', models.TextField(blank=True, default='')),
                ('situa1', models.TextField(blank=True, default='')),
                ('piclink', models.TextField(blank=True, default='')),
                ('expop', models.CharField(max_length=200)),
                ('leader', models.CharField(default='m', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='casehistory',
        ),
    ]