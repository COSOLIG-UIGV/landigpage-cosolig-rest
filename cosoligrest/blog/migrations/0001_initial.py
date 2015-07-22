# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_publicacion', models.DateTimeField(default=datetime.datetime(2015, 7, 22, 21, 37, 56, 821446, tzinfo=utc))),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
            ],
        ),
    ]
