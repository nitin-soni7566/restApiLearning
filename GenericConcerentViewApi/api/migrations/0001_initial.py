# Generated by Django 4.1.3 on 2022-12-10 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_class', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
