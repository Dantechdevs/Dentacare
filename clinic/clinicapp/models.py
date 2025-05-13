from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Specialty(models.Model):
    """Medical specialization hierarchy with WHO standards"""
    name = models.CharField(
        _("Medical Specialty"),
        max_length=100,
        unique=True,
        help_text=_("WHO-recognized medical specialty")
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subspecialties',
        verbose_name=_("Parent Specialty")
    )
    icd_code = models.CharField(
        _("ICD-11 Code"),
        max_length=8,
        blank=True,
        help_text=_("International Classification of Diseases code")
    )

    class Meta:
        verbose_name = _("Medical Specialty")
        verbose_name_plural = _("Medical Specialties")
        ordering = ['name']

    def __str__(self):
        return f"{self.name} [{self.icd_code}]" if self.icd_code else self.name


class Language(models.Model):
    """ISO 639-2 language codes with clinical context support"""
    ISO_639_2_CHOICES = [
        ('eng', 'English'),
        ('kisw', 'Kiswahili'),
        ('ara', 'Arabic'),
        ('spa', 'Spanish'),
        ('fra', 'French'),
        # Add more medical-relevant languages as needed
    ]

    code = models.CharField(
        _("ISO 639-2 Code"),
        max_length=4,  # ✅ Increased from 3 to 4
        choices=ISO_639_2_CHOICES,
        unique=True
    )
    name = models.CharField(
        _("Display Name"),
        max_length=50,
        editable=False
    )

    class Meta:
        verbose_name = _("Clinical Language")
        verbose_name_plural = _("Clinical Languages")
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.name = dict(self.ISO_639_2_CHOICES).get(self.code, 'Unknown')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Doctor(models.Model):
    """Core medical practitioner model with extended capabilities"""
    license_number = models.CharField(
        _("Medical License Number"),
        max_length=20,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{2}-\d{6}$',
                message=_("Format: CC-123456 (Country Code-Digits)"),
            )
        ]
    )
    title = models.CharField(
        _("Professional Title"),
        max_length=10,
        choices=[
            ('Dr', _('Doctor')),
            ('Prof', _('Professor')),
            ('Sr', _('Surgeon')),
        ]
    )
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)

    emergency_contact = models.CharField(
        _("Emergency Contact"),
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?[1-9]\d{1,14}$',
                message=_("Enter valid E.164 format phone number")
            )
        ]
    )
    clinical_email = models.EmailField(
        _("Clinical Email"),
        unique=True,
        help_text=_("For patient communications")
    )

    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.PROTECT,
        related_name='practitioners',
        verbose_name=_("Primary Specialty")
    )
    qualifications = models.TextField(
        _("Medical Qualifications"),
        help_text=_("Comma-separated list of degrees/certifications")
    )
    experience_years = models.PositiveIntegerField(
        _("Years of Experience"),
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )

    working_hours = models.JSONField(
        _("Clinical Schedule"),
        default=dict,
        blank=True,
        help_text=_("""JSON structure format:
        {
            "day": {
                "sessions": [
                    {"start": "HH:MM", "end": "HH:MM", "type": "consultation"},
                    {"start": "HH:MM", "end": "HH:MM", "type": "emergency"}
                ],
                "closed": false
            }
        }""")
    )

    languages_spoken = models.ManyToManyField(
        Language,
        verbose_name=_("Patient Languages"),
        related_name='doctors',
        help_text=_("Select languages used for clinical communication")
    )

    primary_hospital = models.CharField(
        _("Primary Hospital"),
        max_length=100,
        blank=True
    )
    alternate_hospitals = models.TextField(
        _("Affiliated Institutions"),
        blank=True,
        help_text=_("Comma-separated list of hospitals/clinics")
    )

    class Meta:
        verbose_name = _("Medical Practitioner")
        verbose_name_plural = _("Medical Practitioners")
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['license_number']),
        ]
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('doctor-detail', args=[str(self.id)])

    @property
    def available_days(self):
        return [day for day, hours in self.working_hours.items() if not hours.get('closed')]

    def get_working_hours_display(self):
        return "\n".join(
            f"{day}: {', '.join(session['type'] for session in hours.get('sessions', []))}"
            for day, hours in self.working_hours.items()
        )
