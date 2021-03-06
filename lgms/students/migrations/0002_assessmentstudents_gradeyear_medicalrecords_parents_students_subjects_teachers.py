# Generated by Django 2.0.6 on 2018-06-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentsname', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('assessmentinfo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GradeYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentcondition', models.CharField(max_length=30)),
                ('illnessinfo', models.CharField(max_length=30)),
                ('hospitalizationinfo', models.CharField(max_length=30)),
                ('accident_injury', models.CharField(max_length=30)),
                ('immunizationinfo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('studentsname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]
