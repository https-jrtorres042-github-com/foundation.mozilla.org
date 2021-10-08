# Generated by Django 3.1.11 on 2021-10-11 23:40

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0042_productpage_tips_to_protect_yourself'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='blurb',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Description of the product', max_length=5000),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='worst_case',
            field=wagtail.core.fields.RichTextField(blank=True, help_text="What's the worst thing that could happen by using this product?", max_length=5000),
        ),
    ]