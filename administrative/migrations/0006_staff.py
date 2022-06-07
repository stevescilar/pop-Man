# Generated by Django 4.0.5 on 2022-06-07 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrative', '0005_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('contact', models.CharField(blank=True, max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('teacher_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrative.class', verbose_name='Class')),
            ],
        ),
    ]
