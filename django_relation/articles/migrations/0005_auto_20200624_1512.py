# Generated by Django 3.0.7 on 2020-06-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='%y/%m/%d/'),
        ),
    ]
