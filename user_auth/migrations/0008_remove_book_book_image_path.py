# Generated by Django 4.1.7 on 2023-03-07 10:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_auth", "0007_book_book_image_path"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="book_image_path",
        ),
    ]
