# Generated by Django 4.1.2 on 2022-11-01 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_alter_task_kat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="kat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="main.kategoria"
            ),
        ),
    ]
