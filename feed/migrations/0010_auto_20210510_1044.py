# Generated by Django 3.1.7 on 2021-05-10 08:44

from django.db import migrations, models
import feed.validators


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_auto_20210408_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, upload_to='path/to/video', validators=[feed.validators.file_size]),
        ),
    ]
