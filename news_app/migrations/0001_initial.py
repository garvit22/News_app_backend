# Generated by Django 5.0.2 on 2025-04-06 14:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_searched', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-last_searched'],
                'unique_together': {('keyword', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('published_at', models.DateTimeField()),
                ('source_name', models.CharField(max_length=255)),
                ('source_category', models.CharField(blank=True, max_length=100, null=True)),
                ('language', models.CharField(default='en', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('search_keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='news_app.searchkeyword')),
            ],
            options={
                'ordering': ['-published_at'],
                'indexes': [models.Index(fields=['published_at'], name='news_app_ar_publish_931598_idx'), models.Index(fields=['source_name'], name='news_app_ar_source__cdc6fa_idx'), models.Index(fields=['language'], name='news_app_ar_languag_08370d_idx')],
            },
        ),
    ]
