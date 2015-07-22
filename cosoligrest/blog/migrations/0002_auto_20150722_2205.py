# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 22, 5, 41, 437246, tzinfo=utc)),
        ),
    ]
