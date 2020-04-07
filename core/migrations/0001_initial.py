# Generated by Django 3.0.4 on 2020-04-07 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '__first__'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Date Range Filter')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=512)),
                ('images', models.CharField(max_length=512)),
                ('subscription_fee', models.PositiveIntegerField()),
                ('no_of_tickets', models.PositiveIntegerField()),
                ('sold_tickets', models.PositiveIntegerField(default=0)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('external_links', models.CharField(max_length=1024)),
                ('event_created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Date Range Filter')),
                ('type', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Date Range Filter')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True)),
                ('organization', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('role', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Date Range Filter')),
                ('no_of_tickets', models.PositiveIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Event')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='payment.Payment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Date Range Filter')),
                ('discount_percentage', models.PositiveIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Date Range Filter')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.EventType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.EventType'),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('name', 'type', 'date', 'time')},
        ),
    ]
