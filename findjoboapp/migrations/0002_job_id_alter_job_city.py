# Generated by Django 4.1.3 on 2022-11-19 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('findjoboapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='id',
            field=models.BigAutoField(auto_created=True,  primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='findjoboapp.city'),
        ),
    ]
