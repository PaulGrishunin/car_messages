# Generated by Django 3.2.7 on 2021-09-16 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('reg_number', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('tel_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('received', models.BooleanField(default=False)),
                ('read', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.car')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.owner')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='owners',
            field=models.ManyToManyField(to='app.Owner'),
        ),
    ]
