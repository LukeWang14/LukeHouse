# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MOOC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('AnnouncementContent', models.CharField(max_length=50)),
                ('CreatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('FromChapter', models.ForeignKey(to='MOOC.Chapter')),
            ],
        ),
    ]
