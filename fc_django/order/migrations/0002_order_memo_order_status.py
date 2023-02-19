# Generated by Django 4.1.7 on 2023-02-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="memo",
            field=models.TextField(blank=True, null=True, verbose_name="메모"),
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(default="대기중", max_length=32, verbose_name="상태"),
        ),
    ]
