# Generated by Django 3.0.4 on 2020-03-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100000)),
                ('summary', models.TextField(default='It is the summary')),
                ('is_sold', models.BooleanField(default=True)),
            ],
        ),
    ]