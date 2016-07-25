# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('AnswerContent', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ChapterNum', models.IntegerField()),
                ('ChapterName', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Name', models.CharField(default='', max_length=30)),
                ('ValidOrNot', models.IntegerField()),
                ('Introduction', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Title', models.CharField(max_length=50)),
                ('Content', models.CharField(default='', max_length=500)),
                ('FromChapter', models.ForeignKey(to='MOOC.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('QuestionTitle', models.CharField(default='', max_length=50)),
                ('QuestionContent', models.CharField(default='', max_length=500)),
                ('FromChapter', models.ForeignKey(to='MOOC.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('username', models.CharField(default='', max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(default='肖冬', max_length=50)),
                ('school', models.CharField(default='清华大学', max_length=50)),
                ('studentnum', models.CharField(default='2014013424', max_length=50)),
                ('teachernum', models.CharField(default='2014013424', max_length=50)),
                ('selfintroduction', models.CharField(default='这是我的个人简介', max_length=400)),
                ('Type', models.CharField(default='student', max_length=50)),
                ('StuProfession', models.CharField(default='softwareengineering', max_length=30)),
                ('TeaProfession', models.CharField(default='softwareengineering', max_length=30)),
                ('CourseList', models.ManyToManyField(to='MOOC.Course')),
                ('StuList', models.ManyToManyField(to='MOOC.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
            field=models.ManyToManyField(to='MOOC.Category'),
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
