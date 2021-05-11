# Generated by Django 3.2.2 on 2021-05-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(default='John', max_length=20)),
                ('last_name', models.CharField(default='Doe', max_length=20)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], default='not sepcified', max_length=10)),
                ('occupation', models.CharField(choices=[('d', 'developer'), ('m', 'mechanic'), ('w', 'welder'), ('p', 'plumber')], default='not sepcified', max_length=20)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
