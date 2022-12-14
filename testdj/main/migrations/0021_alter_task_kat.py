# Generated by Django 4.1.2 on 2022-11-02 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0020_remove_task_kat_s"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="kat",
            field=models.ForeignKey(
                help_text="Выберите категорию",
                on_delete=django.db.models.deletion.PROTECT,
                to="main.kategoria",
            ),
        ),
    ]
