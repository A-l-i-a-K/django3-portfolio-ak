# Generated by Django 4.1 on 2022-09-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='portfolio.ipmodel'),
        ),
    ]
