# Generated by Django 2.1.2 on 2019-01-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enter_Username', models.CharField(max_length=30)),
                ('Enter_Password', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
