# Generated by Django 2.0.5 on 2023-01-23 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labelresult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(max_length=50, verbose_name='自定义id')),
                ('img_name', models.ImageField(blank=True, null=True, upload_to='', verbose_name='图片文件')),
                ('txt', models.TextField(verbose_name='文本')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='标记时间')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '标注记录',
                'verbose_name_plural': '标注记录',
            },
        ),
        migrations.CreateModel(
            name='LabelTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_done', models.IntegerField(choices=[(0, '未标注'), (1, '跳过'), (2, '完成')], default=0, verbose_name='是否完成')),
            ],
            options={
                'verbose_name': '任务分配',
                'verbose_name_plural': '任务分配',
            },
        ),
    ]