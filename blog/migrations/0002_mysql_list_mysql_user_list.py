# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mysql_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ip', models.GenericIPAddressField()),
                ('mysqltype', models.SmallIntegerField(verbose_name='数据库类型', choices=[(1, '主库'), (2, '从库')])),
                ('username', models.CharField(verbose_name='帐号', max_length=64, default='')),
                ('password', models.CharField(verbose_name='密码', max_length=64, default='')),
                ('port', models.IntegerField(verbose_name='端口号', default=3306)),
                ('master_ip', models.GenericIPAddressField(blank=True, null=True, default='')),
                ('master_port', models.IntegerField(verbose_name='主库端口号', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mysql_user_list',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userlist', models.TextField(verbose_name='用户列表', blank=True, null=True)),
                ('db_id', models.ForeignKey(to='blog.mysql_list')),
            ],
        ),
    ]
