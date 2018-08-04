# Generated by Django 2.0.6 on 2018-07-11 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0060_auto_20180711_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SPED', 'Special Education Program'), ('GS', 'Grade School Program'), ('CA', 'CASA Program'), ('SH', 'Senior High School Program'), ('JH', 'Junior High School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='childsname',
            field=models.CharField(blank=True, max_length=64, verbose_name='Childsname'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('D', 'Divorcee'), ('W', 'Widowed'), ('M', 'Married'), ('SP', 'Single Parent')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('C', 'Catholic'), ('B', 'Buddhist'), ('M', 'Muslim')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='parentsinfo',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('C', 'Catholic'), ('B', 'Buddhist'), ('M', 'Muslim')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='studentbio',
            name='studentname',
            field=models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, to='students.Students'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('G1', 'GRADE 1'), ('G9', 'GRADE 9'), ('G4', 'GRADE 4'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('G2', 'GRADE 2'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('CM', 'CASA AM'), ('G3', 'GRADE 3'), ('TEP', 'TEACH PM'), ('G10', 'GRADE 10'), ('G5', 'GRADE 5'), ('G7', 'GRADE 7'), ('TEA', 'TEACH AM'), ('TEP-GR2', 'TEACH PM GRADE 2'), ('PG', 'PLAY GROUP'), ('CA', 'CASA AFTERNOON 1:30'), ('G8', 'GRADE 8'), ('G6', 'GRADE 6')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
    ]