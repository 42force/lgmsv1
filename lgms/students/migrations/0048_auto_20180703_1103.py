# Generated by Django 2.0.6 on 2018-07-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0047_auto_20180702_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentbio',
            name='charactersets',
            field=models.ManyToManyField(to='students.CharacterBuildingActivities'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SH', 'Senior High School Program'), ('CA', 'CASA Program'), ('SPED', 'Special Education Program'), ('JH', 'Junior High School Program'), ('GS', 'Grade School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('D', 'Divorcee'), ('W', 'Widowed'), ('SP', 'Single Parent'), ('M', 'Married')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('C', 'Catholic'), ('M', 'Muslim'), ('B', 'Buddhist')], default='C', help_text='Please select your Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('G3', 'GRADE 3'), ('G10', 'GRADE 10'), ('G4', 'GRADE 4'), ('G5', 'GRADE 5'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('G6', 'GRADE 6'), ('CA', 'CASA AFTERNOON 1:30'), ('TEP', 'TEACH PM'), ('G2', 'GRADE 2'), ('G7', 'GRADE 7'), ('G8', 'GRADE 8'), ('TEP-GR2', 'TEACH PM GRADE 2'), ('PG', 'PLAY GROUP'), ('G9', 'GRADE 9'), ('G1', 'GRADE 1'), ('CM', 'CASA AM'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('TEA', 'TEACH AM')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('SH', 'SCHOOL HEAD'), ('F', 'FACULTY'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]
