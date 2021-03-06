# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2020-12-10 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_rawhtml', '0003_fourcolumnrawhtmlplugindata_threecolumnrawhtmlplugindata_twocolumnrawhtmlplugindata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourcolumnrawhtmlplugindata',
            name='body_left',
            field=models.TextField(verbose_name='HTML left'),
        ),
        migrations.AlterField(
            model_name='fourcolumnrawhtmlplugindata',
            name='body_middle_left',
            field=models.TextField(verbose_name='HTML middle left'),
        ),
        migrations.AlterField(
            model_name='fourcolumnrawhtmlplugindata',
            name='body_middle_right',
            field=models.TextField(verbose_name='HTML middle right'),
        ),
        migrations.AlterField(
            model_name='fourcolumnrawhtmlplugindata',
            name='body_right',
            field=models.TextField(verbose_name='HTML right'),
        ),
        migrations.AlterField(
            model_name='threecolumnrawhtmlplugindata',
            name='body_left',
            field=models.TextField(verbose_name='HTML left'),
        ),
        migrations.AlterField(
            model_name='threecolumnrawhtmlplugindata',
            name='body_middle',
            field=models.TextField(verbose_name='HTML middle'),
        ),
        migrations.AlterField(
            model_name='threecolumnrawhtmlplugindata',
            name='body_right',
            field=models.TextField(verbose_name='HTML right'),
        ),
        migrations.AlterField(
            model_name='twocolumnrawhtmlplugindata',
            name='body_left',
            field=models.TextField(verbose_name='HTML left'),
        ),
        migrations.AlterField(
            model_name='twocolumnrawhtmlplugindata',
            name='body_right',
            field=models.TextField(verbose_name='HTML right'),
        ),
    ]
