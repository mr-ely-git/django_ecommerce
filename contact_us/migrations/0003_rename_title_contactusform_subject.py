# Generated by Django 4.2.3 on 2023-08-13 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_alter_contactusform_is_read_by_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactusform',
            old_name='title',
            new_name='subject',
        ),
    ]
