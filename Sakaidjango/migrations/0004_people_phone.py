# Generated by Django 4.2.3 on 2023-07-28 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sakaidjango', '0003_people_delete_student_delete_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='phone',
            field=models.IntegerField(default=1, max_length=30),
        ),
    ]
