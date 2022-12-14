# Generated by Django 4.1.2 on 2022-11-01 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_task_kat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="kat",
            field=models.ForeignKey(
                choices=[
                    ("", "Выберите категорию обращения"),
                    ("Замена Картриджа", "Замена Картриджа"),
                    (
                        "Устранение неполадок с техникой",
                        "Устранение неполадок с техникой",
                    ),
                    ("Выдача оборудования", "Выдача оборудования"),
                    ("Другое", "Другое"),
                ],
                on_delete=django.db.models.deletion.PROTECT,
                to="main.kategoria",
            ),
        ),
    ]
