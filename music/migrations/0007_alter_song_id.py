# Generated by Django 3.2.7 on 2021-09-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
