from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class Occupation(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MedicalProfessional(models.Model):
    # Kenya's 47 counties + capitals (shortened here for brevity; full list below)
    COUNTY_CHOICES = [
    ('KE-01', 'Mombasa'),
    ('KE-02', 'Kwale'),
    ('KE-03', 'Kilifi'),
    ('KE-04', 'Tana River'),
    ('KE-05', 'Lamu'),
    ('KE-06', 'Taita-Taveta'),
    ('KE-07', 'Garissa'),
    ('KE-08', 'Wajir'),
    ('KE-09', 'Mandera'),
    ('KE-10', 'Marsabit'),
    ('KE-11', 'Isiolo'),
    ('KE-12', 'Meru'),
    ('KE-13', 'Tharaka-Nithi'),
    ('KE-14', 'Embu'),
    ('KE-15', 'Kitui'),
    ('KE-16', 'Machakos'),
    ('KE-17', 'Makueni'),
    ('KE-18', 'Nyandarua'),
    ('KE-19', 'Nyeri'),
    ('KE-20', 'Kirinyaga'),
    ('KE-21', 'Murang\'a'),
    ('KE-22', 'Kiambu'),
    ('KE-23', 'Turkana'),
    ('KE-24', 'West Pokot'),
    ('KE-25', 'Samburu'),
    ('KE-26', 'Trans-Nzoia'),
    ('KE-27', 'Uasin Gishu'),
    ('KE-28', 'Elgeyo-Marakwet'),
    ('KE-29', 'Nandi'),
    ('KE-30', 'Baringo'),
    ('KE-31', 'Laikipia'),
    ('KE-32', 'Nakuru'),
    ('KE-33', 'Narok'),
    ('KE-34', 'Kajiado'),
    ('KE-35', 'Kericho'),
    ('KE-36', 'Bomet'),
    ('KE-37', 'Kakamega'),
    ('KE-38', 'Vihiga'),
    ('KE-39', 'Bungoma'),
    ('KE-40', 'Busia'),
    ('KE-41', 'Siaya'),
    ('KE-42', 'Kisumu'),
    ('KE-43', 'Homa Bay'),
    ('KE-44', 'Migori'),
    ('KE-45', 'Kisii'),
    ('KE-46', 'Nyamira'),
    ('KE-47', 'Nairobi'),
]

    STATUS_CHOICES = [
        ('ACT', _('Active')),
        ('LVE', _('On Leave')),
        ('RET', _('Retired')),
        ('SUS', _('Suspended')),
    ]

    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Surname"), max_length=50)
    email = models.EmailField(_("Work Email"), unique=True)
    phone = models.CharField(
        _("Mobile Number"),
        max_length=10,
        validators=[RegexValidator(regex=r'^07\d{8}$', message=_("Enter 10-digit Safaricom number starting with 07"))]
    )
    county = models.CharField(_("County of Practice"), max_length=5, choices=COUNTY_CHOICES)
    status = models.CharField(_("Employment Status"), max_length=3, choices=STATUS_CHOICES, default='ACT')
    license_number = models.CharField(_("Medical License"), max_length=20, unique=True, blank=True)
    
    occupation = models.ForeignKey(Occupation, on_delete=models.SET_NULL, null=True, verbose_name=_("Medical Specialty"))

    address = models.CharField(_("Clinic Address"), max_length=255, blank=True)
    bio = models.TextField(_("Professional Biography"), blank=True)
    avatar = models.ImageField(_("Profile Photo"), upload_to='professionals/avatars/', default='default/medical-professional.png')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _("Medical Practitioner")
        verbose_name_plural = _("Medical Practitioners")
        indexes = [
            models.Index(fields=['occupation']),
        ]

    def __str__(self):
        return f"{self.occupation} {self.last_name.upper()}, {self.first_name}"



