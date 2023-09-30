# Generated by Django 4.1.7 on 2023-09-30 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('property', models.CharField(max_length=100)),
                ('level', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='blogcontents',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog.category'),
        ),
        migrations.AlterField(
            model_name='blogcontents',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='blog.category'),
        ),
    ]
