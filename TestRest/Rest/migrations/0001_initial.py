# Generated by Django 3.0.8 on 2020-09-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('transection_date', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('Order_no', models.IntegerField()),
                ('customer_Id', models.IntegerField()),
                ('UDID_id', models.UUIDField(default='uuid.uuid4', editable=False, primary_key=True, serialize=False)),
                ('date_recieve', models.IntegerField()),
                ('tranjection_code', models.IntegerField()),
                ('tranjection_text', models.CharField(max_length=200)),
            ],
        ),
    ]