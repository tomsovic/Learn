# Generated by Django 2.2.5 on 2019-09-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, help_text='文章标题', max_length=100, verbose_name='标题')),
                ('content', models.TextField(help_text='正文内容', verbose_name='正文')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('auth', models.CharField(max_length=50, verbose_name='作者')),
                ('source', models.CharField(blank=True, max_length=200, null=True, verbose_name='来源')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章',
                'db_table': 'article',
                'ordering': ['-id'],
            },
        ),
    ]
