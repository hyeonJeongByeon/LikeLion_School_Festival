# Generated by Django 2.2.1 on 2019-05-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190511_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='busy',
            field=models.CharField(choices=[('혼잡', '혼잡'), ('보통', '보통'), ('여유', '여유')], max_length=50),
        ),
    ]
