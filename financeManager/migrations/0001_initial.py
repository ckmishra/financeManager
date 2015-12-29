# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='financeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('policyNumber', models.CharField(max_length=20, unique=True)),
                ('financeType', models.CharField(max_length=20)),
                ('issueDate', models.DateField()),
                ('maturityDate', models.DateField()),
                ('amount', models.IntegerField()),
                ('remarks', models.CharField(max_length=200)),
                ('userName', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
