# Generated by Django 2.2 on 2019-07-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBFApp', '0012_auto_20190719_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=350, max_digits=8),
        ),
    ]