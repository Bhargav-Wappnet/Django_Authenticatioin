# Generated by Django 4.1.7 on 2023-03-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_auth", "0006_alter_book_book_author_alter_book_book_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="book_image_path",
            field=models.CharField(default=None, max_length=255),
        ),
    ]
