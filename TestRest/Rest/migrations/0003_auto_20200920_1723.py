# Generated by Django 3.0.8 on 2020-09-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rest', '0002_auto_20200920_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_recieve',
            field=models.DateField(blank=True, default='', help_text='today date.', null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transection_date',
            field=models.DateField(default='', help_text='today date.', null=True),
        ),
    ]