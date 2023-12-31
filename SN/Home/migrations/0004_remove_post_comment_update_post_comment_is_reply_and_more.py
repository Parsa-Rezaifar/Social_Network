# Generated by Django 4.2.4 on 2023-09-04 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_comment',
            name='update',
        ),
        migrations.AddField(
            model_name='post_comment',
            name='is_reply',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post_comment',
            name='reply_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_comments', to='Home.post_comment'),
        ),
    ]
