# Generated by Django 2.2.24 on 2021-09-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210917_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(default='student.png', upload_to='profile_pic/Customer/'),
        ),
    ]
