# Generated by Django 3.0.8 on 2020-09-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rest', '0004_auto_20200920_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdataile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transection_date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField()),
                ('Order_no', models.IntegerField()),
                ('customer_Id', models.IntegerField()),
                ('f', models.CharField(default='generateUUID', editable=False, max_length=36, unique=True)),
                ('date_recieve', models.DateField(blank=True, null=True)),
                ('tranjection_code', models.IntegerField()),
                ('tranjection_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
