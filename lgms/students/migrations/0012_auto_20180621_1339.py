# Generated by Django 2.0.6 on 2018-06-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20180621_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gradeyear',
            field=models.CharField(choices=[('1', 'GRADE 1'), ('2', 'GRADE 2'), ('3', 'GRADE 3'), ('4', 'GRADE 4'), ('5', 'GRADE 5'), ('6', 'GRADE 6'), ('7', 'GRADE 7'), ('8', 'GRADE 8'), ('9', 'GRADE 9'), ('10', 'GRADE 10')], default='1', max_length=10, verbose_name='Grade Choice'),
        ),
    ]
