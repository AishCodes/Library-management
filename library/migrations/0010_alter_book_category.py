# Generated by Django 4.0.3 on 2023-04-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20230228_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('programming', 'Programming'), ('media', 'Media'), ('business', 'Business'), ('communication', 'Communication')], default='education', max_length=30),
        ),
    ]
