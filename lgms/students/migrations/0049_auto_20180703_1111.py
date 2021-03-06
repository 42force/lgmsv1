# Generated by Django 2.0.6 on 2018-07-03 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0048_auto_20180703_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('JH', 'Junior High School Program'), ('SPED', 'Special Education Program'), ('GS', 'Grade School Program'), ('CA', 'CASA Program'), ('SH', 'Senior High School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('SP', 'Single Parent'), ('D', 'Divorcee'), ('M', 'Married'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('M', 'Muslim'), ('B', 'Buddhist'), ('I', 'INC'), ('C', 'Catholic')], default='C', help_text='Please select your Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='studentbio',
            name='gradeyear',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='gradeyear_gradeyear', to='students.GradeYear'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('TEP-GR2', 'TEACH PM GRADE 3'), ('CA', 'CASA AFTERNOON 1:30'), ('G1', 'GRADE 1'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('G2', 'GRADE 2'), ('G7', 'GRADE 7'), ('G5', 'GRADE 5'), ('G6', 'GRADE 6'), ('G4', 'GRADE 4'), ('G9', 'GRADE 9'), ('G10', 'GRADE 10'), ('TEP-GR2', 'TEACH PM GRADE 2'), ('PG', 'PLAY GROUP'), ('CM', 'CASA AM'), ('G8', 'GRADE 8'), ('TEP', 'TEACH PM'), ('G3', 'GRADE 3'), ('TEA', 'TEACH AM')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('S', 'STAFF'), ('F', 'FACULTY'), ('SH', 'SCHOOL HEAD')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]
