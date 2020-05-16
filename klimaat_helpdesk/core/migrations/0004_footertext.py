# Generated by Django 3.0.5 on 2020-05-16 12:37

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_gitlabissues'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', wagtail.core.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Footer Text',
            },
        ),
    ]