# Generated by Django 4.2.3 on 2023-07-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sakaidjango', '0005_alter_people_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='city',
            field=models.CharField(default='nairobi', max_length=9),
        ),
        migrations.AddField(
            model_name='people',
            name='country',
            field=models.CharField(default='kenya', max_length=9),
        ),
        migrations.AlterField(
            model_name='people',
            name='age',
            field=models.CharField(max_length=20),
        ),
    ]
