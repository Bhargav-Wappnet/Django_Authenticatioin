# Generated by Django 4.1.7 on 2023-03-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_auth", "0002_alter_customuser_image_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]