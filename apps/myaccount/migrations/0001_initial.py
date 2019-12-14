# Generated by Django 2.2.4 on 2019-12-14 18:22
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        if User.objects.count() == 0:
            superuser = User.objects.create_superuser(
                username="admin",
                email="admin@local",
                password="admin")
            superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
