# Generated by Django 5.1.1 on 2025-05-15 12:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalProfessional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Surname')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Work Email')),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Enter 10-digit Safaricom number starting with 07', regex='^07\\d{8}$')], verbose_name='Mobile Number')),
                ('county', models.CharField(choices=[('KE-01', 'Mombasa'), ('KE-02', 'Kwale'), ('KE-03', 'Kilifi'), ('KE-04', 'Tana River'), ('KE-05', 'Lamu'), ('KE-06', 'Taita-Taveta'), ('KE-07', 'Garissa'), ('KE-08', 'Wajir'), ('KE-09', 'Mandera'), ('KE-10', 'Marsabit'), ('KE-11', 'Isiolo'), ('KE-12', 'Meru'), ('KE-13', 'Tharaka-Nithi'), ('KE-14', 'Embu'), ('KE-15', 'Kitui'), ('KE-16', 'Machakos'), ('KE-17', 'Makueni'), ('KE-18', 'Nyandarua'), ('KE-19', 'Nyeri'), ('KE-20', 'Kirinyaga'), ('KE-21', "Murang'a"), ('KE-22', 'Kiambu'), ('KE-23', 'Turkana'), ('KE-24', 'West Pokot'), ('KE-25', 'Samburu'), ('KE-26', 'Trans-Nzoia'), ('KE-27', 'Uasin Gishu'), ('KE-28', 'Elgeyo-Marakwet'), ('KE-29', 'Nandi'), ('KE-30', 'Baringo'), ('KE-31', 'Laikipia'), ('KE-32', 'Nakuru'), ('KE-33', 'Narok'), ('KE-34', 'Kajiado'), ('KE-35', 'Kericho'), ('KE-36', 'Bomet'), ('KE-37', 'Kakamega'), ('KE-38', 'Vihiga'), ('KE-39', 'Bungoma'), ('KE-40', 'Busia'), ('KE-41', 'Siaya'), ('KE-42', 'Kisumu'), ('KE-43', 'Homa Bay'), ('KE-44', 'Migori'), ('KE-45', 'Kisii'), ('KE-46', 'Nyamira'), ('KE-47', 'Nairobi')], max_length=5, verbose_name='County of Practice')),
                ('status', models.CharField(choices=[('ACT', 'Active'), ('LVE', 'On Leave'), ('RET', 'Retired'), ('SUS', 'Suspended')], default='ACT', max_length=3, verbose_name='Employment Status')),
                ('license_number', models.CharField(blank=True, max_length=20, unique=True, verbose_name='Medical License')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Clinic Address')),
                ('bio', models.TextField(blank=True, verbose_name='Professional Biography')),
                ('avatar', models.ImageField(default='default/medical-professional.png', upload_to='professionals/avatars/', verbose_name='Profile Photo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('occupation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinicapp.occupation', verbose_name='Medical Specialty')),
            ],
            options={
                'verbose_name': 'Medical Practitioner',
                'verbose_name_plural': 'Medical Practitioners',
                'ordering': ['last_name', 'first_name'],
                'indexes': [models.Index(fields=['occupation'], name='clinicapp_m_occupat_bfb337_idx')],
            },
        ),
    ]
