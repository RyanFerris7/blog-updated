# Generated by Django 4.2.10 on 2024-02-29 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_excerpt_post_status_post_updated_on_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
