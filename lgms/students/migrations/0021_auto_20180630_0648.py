# Generated by Django 2.0.6 on 2018-06-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_auto_20180627_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='applicationenrolled',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='assesmentsstats',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='gradeenrolled',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='medicalrecords',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='teachersname',
        ),
        migrations.AlterModelOptions(
            name='medicalrecords',
            options={'verbose_name_plural': 'Medical Records'},
        ),
        migrations.RemoveField(
            model_name='parents',
            name='studentsname',
        ),
        migrations.AddField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('M', 'Married'), ('D', 'Divorcee'), ('SP', 'Single Parent'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('M', 'Muslim'), ('C', 'Catholic'), ('I', 'INC'), ('B', 'Buddhist')], default='C', help_text='Please select your Religion', max_length=30),
        ),
        migrations.AddField(
            model_name='parents',
            name='address',
            field=models.CharField(blank=True, max_length=64, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('CA', 'CASA Program'), ('SPED', 'Special Education Program'), ('GS', 'Grade School Program'), ('SH', 'Senior High School Program'), ('JH', 'Junior High School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.DeleteModel(
            name='ClassRoom',
        ),
    ]
