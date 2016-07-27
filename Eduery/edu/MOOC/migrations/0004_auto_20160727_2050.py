# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MOOC', '0003_auto_20160727_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='FromChapter',
        ),
        migrations.AddField(
            model_name='announcement',
            name='FromCourse',
            field=models.ForeignKey(default=2, to='MOOC.Course'),
            preserve_default=False,
        ),
    ]
