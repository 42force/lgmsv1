# Generated by Django 2.0.6 on 2018-07-31 08:46

from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0103_auto_20180731_0412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compute',
            options={'verbose_name_plural': 'Computation Test Only'},
        ),
        migrations.RemoveField(
            model_name='statementaccount',
            name='gtotal_currency',
        ),
        migrations.RemoveField(
            model_name='statementaccount',
            name='modeofpaymenttotal_currency',
        ),
        migrations.RemoveField(
            model_name='statementaccount',
            name='totalprice_currency',
        ),
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('GOOD', 'G'), ('NEEDS IMPROVEMENT', 'NI'), ('UNSATISFACTORY / FAILED', 'U'), ('EXCELLENT', 'E'), ('VERY GOOD', 'VG'), ('FAIR / PASSED', 'F')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=6, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program'), ('GRADE SCHOOL PROGRAM', 'Grade School Program'), ('SPED', 'Special Education Program'), ('CASA PROGRAM', 'CASA Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('W', 'Widowed'), ('M', 'Married'), ('SP', 'Single Parent'), ('D', 'Divorcee')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('M', 'Muslim'), ('C', 'Catholic'), ('B', 'Buddhist')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('DP', 'Dermatology Problem'), ('EPL', 'Epilepsy'), ('DM', 'Diabetes Mellitus'), ('CV', 'Convulsion'), ('GP', 'Gastrointestinal Problems'), ('A', 'Allergy'), ('TP', 'Thyroid Problem'), ('O', 'Others'), ('ANE', 'Anemia'), ('LP', 'Lung Problem'), ('VP', 'Viral Infection'), ('MP', 'Metabolc Problem'), ('AST', 'Asthma'), ('HMP', 'Hematologic Problem'), ('HT', 'Hypertension'), ('SZ', 'Seizures'), ('EP', 'Ear Problems'), ('HP', 'Heart Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('CO', 'COUGH'), ('S', 'STOMACH ACHE'), ('F', 'FEVER'), ('D', 'DIARRHEA'), ('H', 'HEADACHE'), ('C', 'COLDS'), ('0', 'OTHERS'), ('L', 'LBM'), ('V', 'VOMITING')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='bookspricetotal',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='PHP', max_digits=20, verbose_name='Books Price Total'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='discount',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='PHP', max_digits=20, verbose_name='Discount Fee'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='gtotal',
            field=models.IntegerField(default='1234', verbose_name='Grand Total Price'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('SA', 'SEMI-ANNUAL'), ('A', 'ANNUAL'), ('QRT', 'QUARTERLY')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpaymentprice',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='PHP', max_digits=20, verbose_name='Mode of Payment Price'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpaymenttotal',
            field=models.IntegerField(default='1234', verbose_name='Mode Payment Total'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='musicclassprice',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='PHP', max_digits=20, verbose_name='Music Class Price'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='notebooks',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='PHP', max_digits=20, verbose_name='Notebook Price'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='other',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='PHP', max_digits=20, verbose_name='Miscellaneous & Others'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='reservationfee',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='PHP', max_digits=20, verbose_name='Reservation Fee'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='totalprice',
            field=models.IntegerField(default='1234', verbose_name='Total Payment Price'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='uniforms',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='PHP', max_digits=20, verbose_name='Uniform Price'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('76', 'B'), ('87-91', 'P'), ('77-81', 'D'), ('97-100', 'E'), ('82-86', 'AP'), ('92-96', 'A')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('PLAY GROUP', 'PG'), ('GRADE 4', 'G4'), ('GRADE 10', 'G10'), ('GRADE 3', 'G3'), ('GRADE 8', 'G8'), ('CASA AFTERNOON 1:30', 'CA'), ('TEACH PM GRADE 2', 'TEP-GR2'), ('CASA AM', 'CM'), ('TEACH AM', 'TEA'), ('TEACH PM GRADE 1', 'TEP=GR1'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('GRADE 6', 'G6'), ('GRADE 9', 'G9'), ('TEACH PM', 'TEP'), ('GRADE 2', 'G2'), ('GRADE 7', 'G7'), ('GRADE 1', 'G1'), ('GRADE 5', 'G5')], default='CASA AM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('F', 'FACULTY'), ('S', 'STAFF'), ('SH', 'SCHOOL HEAD')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]
