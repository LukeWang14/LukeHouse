# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('AnswerContent', models.CharField(max_length=1000, default='')),
                ('CreatedAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=40, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('ChapterNum', models.IntegerField()),
                ('ChapterName', models.CharField(max_length=40, default='')),
                ('Introduction', models.CharField(max_length=100, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=30, default='')),
                ('ValidOrNot', models.IntegerField()),
                ('Introduction', models.CharField(max_length=500, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Title', models.CharField(max_length=50, default='')),
                ('Content', models.CharField(max_length=500, default='')),
                ('CreatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('FromChapter', models.ForeignKey(to='MOOC.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('QuestionTitle', models.CharField(max_length=50, default='')),
                ('QuestionContent', models.CharField(max_length=500, default='')),
                ('CreatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('FromChapter', models.ForeignKey(to='MOOC.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=50, default='')),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, default='肖冬')),
                ('school', models.CharField(max_length=50, default='清华大学')),
                ('studentnum', models.CharField(max_length=50, default='2014013424')),
                ('teachernum', models.CharField(max_length=50, default='2014013424')),
                ('selfintroduction', models.CharField(max_length=400, default='这是我的个人简介')),
                ('Type', models.CharField(max_length=50, default='student')),
                ('StuProfession', models.CharField(max_length=30, default='softwareengineering')),
                ('TeaProfession', models.CharField(max_length=30, default='softwareengineering')),
                ('CourseList', models.ManyToManyField(to='MOOC.Course')),
                ('StuList', models.ManyToManyField(to='MOOC.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('VideoFile', models.FileField(upload_to='videos')),
                ('FromChapter', models.ForeignKey(to='MOOC.Chapter')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='FromStudent',
            field=models.ForeignKey(to='MOOC.UserInfo'),
        ),
        migrations.AddField(
            model_name='note',
            name='FromStudent',
            field=models.ForeignKey(to='MOOC.UserInfo'),
        ),
        migrations.AddField(
            model_name='course',
            name='InSchool',
            field=models.ForeignKey(to='MOOC.UserInfo'),
        ),
        migrations.AddField(
            model_name='course',
            name='Type',
            field=models.ForeignKey(to='MOOC.Category'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='FromCourse',
            field=models.ForeignKey(to='MOOC.Course'),
        ),
        migrations.AddField(
            model_name='answer',
            name='FromChapter',
            field=models.ForeignKey(to='MOOC.Chapter'),
        ),
        migrations.AddField(
            model_name='answer',
            name='FromTeacher',
            field=models.ForeignKey(to='MOOC.UserInfo'),
        ),
        migrations.AddField(
            model_name='answer',
            name='ToQuestion',
            field=models.ForeignKey(to='MOOC.Question'),
        ),
    ]
