# Generated by Django 4.1.7 on 2023-09-20 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_contact_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('file_name', models.CharField(max_length=100)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('resume_file', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('linked_in', models.URLField()),
                ('insta', models.URLField()),
                ('skype', models.URLField()),
                ('fb', models.URLField()),
                ('twitter_x', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=13)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bio.resume')),
                ('social_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bio.socialprofile')),
            ],
        ),
    ]