# Generated by Django 4.0.7 on 2023-03-08 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='media_type',
            field=models.CharField(choices=[('article', 'Article'), ('book', 'Book'), ('website', 'Website'), ('video', 'Video'), ('other', 'Other')], max_length=50),
        ),
    ]
