# Generated by Django 2.1.7 on 2019-04-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('sname', models.CharField(max_length=20)),
                ('sip', models.CharField(max_length=20)),
                ('submittime', models.DateField()),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
                'db_table': 'studentinfo',
            },
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('tname', models.CharField(max_length=20)),
                ('tpassword', models.CharField(max_length=20)),
                ('admin_flag', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息',
                'db_table': 'teacherinfo',
            },
        ),
    ]
