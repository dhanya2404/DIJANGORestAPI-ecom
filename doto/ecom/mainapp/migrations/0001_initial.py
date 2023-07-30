# Generated by Django 4.2.3 on 2023-07-29 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('Price', models.PositiveIntegerField()),
                ('Image', models.ImageField(upload_to='static/images')),
                ('category', models.CharField(choices=[('tv', 'TV'), ('washingmechine', 'WashingMechine'), ('hplaptop', 'HpLaptop'), ('phone', 'Phone')], max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]