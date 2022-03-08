# Generated by Django 3.2.9 on 2022-03-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0006_ornek'),
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_ismi', models.CharField(max_length=50, verbose_name='kategori isimi')),
            ],
        ),
        migrations.AlterField(
            model_name='ornek',
            name='isim',
            field=models.CharField(max_length=40, verbose_name='İsim Soyisim'),
        ),
    ]
