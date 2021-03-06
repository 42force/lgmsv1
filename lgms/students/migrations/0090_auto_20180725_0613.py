# Generated by Django 2.0.6 on 2018-07-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0089_auto_20180724_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profilepic',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program'), ('GRADE SCHOOL PROGRAM', 'Grade School Program'), ('SPED', 'Special Education Program'), ('CASA PROGRAM', 'CASA Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('D', 'Divorcee'), ('SP', 'Single Parent'), ('M', 'Married'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('B', 'Buddhist'), ('C', 'Catholic'), ('M', 'Muslim')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('SZ', 'Seizures'), ('HP', 'Heart Problem'), ('GP', 'Gastrointestinal Problems'), ('CV', 'Convulsion'), ('LP', 'Lung Problem'), ('HMP', 'Hematologic Problem'), ('TP', 'Thyroid Problem'), ('DP', 'Dermatology Problem'), ('DM', 'Diabetes Mellitus'), ('O', 'Others'), ('HT', 'Hypertension'), ('AST', 'Asthma'), ('EPL', 'Epilepsy'), ('ANE', 'Anemia'), ('VP', 'Viral Infection'), ('EP', 'Ear Problems'), ('A', 'Allergy'), ('MP', 'Metabolc Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('V', 'VOMITING'), ('D', 'DIARRHEA'), ('F', 'FEVER'), ('H', 'HEADACHE'), ('S', 'STOMACH ACHE'), ('CO', 'COUGH'), ('0', 'OTHERS'), ('C', 'COLDS'), ('L', 'LBM')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('TEP-GR2', 'TEACH PM GRADE 2'), ('CA', 'CASA AFTERNOON 1:30'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('G2', 'GRADE 2'), ('G10', 'GRADE 10'), ('TEP', 'TEACH PM'), ('CM', 'CASA AM'), ('G7', 'GRADE 7'), ('G9', 'GRADE 9'), ('G6', 'GRADE 6'), ('G8', 'GRADE 8'), ('PG', 'PLAY GROUP'), ('TEA', 'TEACH AM'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('G5', 'GRADE 5'), ('G4', 'GRADE 4'), ('G1', 'GRADE 1'), ('G3', 'GRADE 3')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
    ]
