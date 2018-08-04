# Generated by Django 2.0.6 on 2018-07-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0026_auto_20180701_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('CA', 'CASA Program'), ('JH', 'Junior High School Program'), ('SPED', 'Special Education Program'), ('GS', 'Grade School Program'), ('SH', 'Senior High School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('W', 'Widowed'), ('D', 'Divorcee'), ('M', 'Married'), ('SP', 'Single Parent')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('M', 'Muslim'), ('B', 'Buddhist'), ('I', 'INC'), ('C', 'Catholic')], default='C', help_text='Please select your Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='name',
            field=models.CharField(blank=True, max_length=64, verbose_name='Teachers Name'),
        ),
    ]
