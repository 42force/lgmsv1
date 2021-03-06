# Generated by Django 2.0.6 on 2018-07-31 23:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0107_auto_20180731_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidentinfo',
            name='endperiodillness',
            field=models.DateField(default=datetime.date.today, verbose_name='Date Ended'),
        ),
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('VERY GOOD', 'VG'), ('UNSATISFACTORY / FAILED', 'U'), ('GOOD', 'G'), ('EXCELLENT', 'E'), ('FAIR / PASSED', 'F'), ('NEEDS IMPROVEMENT', 'NI')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=6, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program'), ('SPED', 'Special Education Program'), ('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('CASA PROGRAM', 'CASA Program'), ('GRADE SCHOOL PROGRAM', 'Grade School Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('SP', 'Single Parent'), ('W', 'Widowed'), ('D', 'Divorcee'), ('M', 'Married')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('B', 'Buddhist'), ('I', 'INC'), ('M', 'Muslim'), ('C', 'Catholic')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('HT', 'Hypertension'), ('DM', 'Diabetes Mellitus'), ('A', 'Allergy'), ('LP', 'Lung Problem'), ('CV', 'Convulsion'), ('DP', 'Dermatology Problem'), ('GP', 'Gastrointestinal Problems'), ('MP', 'Metabolc Problem'), ('EPL', 'Epilepsy'), ('TP', 'Thyroid Problem'), ('ANE', 'Anemia'), ('SZ', 'Seizures'), ('O', 'Others'), ('HP', 'Heart Problem'), ('HMP', 'Hematologic Problem'), ('VP', 'Viral Infection'), ('EP', 'Ear Problems'), ('AST', 'Asthma')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('L', 'LBM'), ('F', 'FEVER'), ('H', 'HEADACHE'), ('S', 'STOMACH ACHE'), ('D', 'DIARRHEA'), ('CO', 'COUGH'), ('0', 'OTHERS'), ('V', 'VOMITING'), ('C', 'COLDS')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('SA', 'SEMI-ANNUAL'), ('QRT', 'QUARTERLY'), ('A', 'ANNUAL')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentbio',
            name='financialinfo',
            field=models.ForeignKey(blank=True, max_length=64, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.StatementAccount', verbose_name='Statement of Account'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('76', 'B'), ('77-81', 'D'), ('97-100', 'E'), ('87-91', 'P'), ('82-86', 'AP'), ('92-96', 'A')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('GRADE 6', 'G6'), ('CASA AM', 'CM'), ('PLAY GROUP', 'PG'), ('GRADE 2', 'G2'), ('TEACH AM', 'TEA'), ('TEACH PM GRADE 1', 'TEP=GR1'), ('TEACH PM', 'TEP'), ('GRADE 4', 'G4'), ('CASA AFTERNOON 1:30', 'CA'), ('GRADE 7', 'G7'), ('GRADE 8', 'G8'), ('GRADE 9', 'G9'), ('GRADE 5', 'G5'), ('GRADE 10', 'G10'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('GRADE 3', 'G3'), ('TEACH PM GRADE 2', 'TEP-GR2'), ('GRADE 1', 'G1')], default='CASA AM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('SH', 'SCHOOL HEAD'), ('F', 'FACULTY'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]
