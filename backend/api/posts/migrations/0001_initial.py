# Generated by Django 2.1.3 on 2018-11-12 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=10)),
                ('src', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('post_identifier', models.CharField(max_length=200)),
                ('platform', models.CharField(max_length=10)),
                ('caption', models.CharField(max_length=400)),
                ('isApproved', models.BooleanField(null=True)),
                ('media', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='posts.Media')),
            ],
        ),
    ]
