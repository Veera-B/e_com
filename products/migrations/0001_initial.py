# Generated by Django 2.2.5 on 2019-09-20 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=30)),
            ],
        ),
    ]
