from django.contrib.gis.db import models  # for adding geospatial fields
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

#from django.db import models

# Create your models here.
class MelghatHamlets23Apr(models.Model):
    geom = models.MultiPointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    srno = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    field_2 = models.CharField(max_length=254, blank=True, null=True)
    state = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    block = models.CharField(max_length=254, blank=True, null=True)
    habitation = models.CharField(max_length=254, blank=True, null=True)
    facility_n = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    file_uploa = models.CharField(max_length=254, blank=True, null=True)
    facility_c = models.CharField(max_length=254, blank=True, null=True)
    facility_s = models.CharField(max_length=254, blank=True, null=True)
    lattitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'melghat_hamlets_23apr'


CHOICES =[('agro','Agro'),
         ('edu','Education'),
         ('med', 'Medical'),
         ('trans', 'Transport/Admin')]

class FeedbackModel(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=10)
    lng = models.DecimalField(max_digits=10, decimal_places=10)
    address = models.CharField(max_length=254)
    #date = models.DateField() #hidden field
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    pin = models.DecimalField(max_digits=6, decimal_places=6)
    domain = models.CharField(max_length=254, choices = CHOICES)
    date = models.DateField()
"""
class feedbackForm(ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['lat', 'lng', 'address', 'city', 'state', 'pin', 'domain', 'date']
        error_messages = {
            'pin': {
                'max_digits': _("This writer's name is too long."),
            },
        }
        """