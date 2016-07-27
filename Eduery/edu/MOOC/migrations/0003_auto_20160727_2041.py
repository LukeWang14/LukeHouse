# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MOOC', '0002_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='AnnouncementContent',
            field=models.CharField(default='当前无公告', max_length=50),
        ),
    ]
