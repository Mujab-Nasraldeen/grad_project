# Generated by Django 2.2.12 on 2020-10-12 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='picture',
            field=models.ImageField(blank=True, default='profiled.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='patient',
            name='picture',
            field=models.ImageField(blank=True, default='profiled.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Doctor'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='patient',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Patient'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='report',
            field=models.TextField(blank=True, null=True),
        ),
    ]