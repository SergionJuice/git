# Generated by Django 4.1.2 on 2022-11-02 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0024_alter_task_kat"),
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
