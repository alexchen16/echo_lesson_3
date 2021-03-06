# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-10 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_name', models.CharField(max_length=255)),
                ('node_type', models.CharField(choices=[('\u603b\u90e8', '\u603b\u90e8'), ('\u5206\u90e8', '\u5206\u90e8')], max_length=50)),
                ('node_address', models.CharField(max_length=255)),
                ('node_contact', models.CharField(max_length=255)),
                ('node_signer', models.CharField(max_length=50)),
                ('node_remarks', models.CharField(blank=True, max_length=255)),
                ('node_signtime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
