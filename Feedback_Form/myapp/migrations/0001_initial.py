# Generated by Django 5.1.3 on 2024-12-26 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('feedback', models.TextField(max_length=1000)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
