# Generated by Django 4.2.6 on 2023-11-10 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="brand_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product.brand",
                verbose_name="Brand",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product.category",
                verbose_name="Category",
            ),
        ),
    ]
