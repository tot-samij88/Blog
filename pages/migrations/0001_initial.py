# Generated by Django 3.1.1 on 2020-09-10 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='photo_for_post')),
                ('title', models.CharField(max_length=200)),
                ('preview_text', models.CharField(max_length=200)),
                ('text_of_post', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('creation_date', models.DateTimeField()),
                ('last_modified', models.DateTimeField()),
            ],
        ),
    ]
