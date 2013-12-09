from django.db import models

class Farmer(models.Model):

    farmer_idx = models.IntegerField(max_length=6)
    farmer_id =  models.CharField(max_length=10, blank=False, default='', primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    alias = models.CharField(max_length=100, blank=True, default='')
    res_address = models.CharField(max_length=200, blank=True, default='')
    res_parish = models.CharField(max_length=20, blank=True, default='')
    tel_number = models.CharField(max_length=20, blank=True, default='')
    cell_number = models.CharField(max_length=20, blank=True, default='')
    verified_status = models.CharField(max_length=3, blank=True, default='')
    dob = models.DateTimeField()
#    reg_date = models.DateTimeField()
    agri_activity = models.CharField(max_length=150, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='farmers')
#    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('dob',)

class Receipt(models.Model):
    farmer_idx = models.IntegerField(max_length=6)
    receipt_no =  models.CharField(max_length=12, blank=False, default='', primary_key=True)
    rec_range1 = models.CharField(max_length=100, blank=True, default='')
    rec_range2 = models.CharField(max_length=100, blank=True, default='')
    investigation_status = models.CharField(max_length=100, blank=True, default='')
    remarks = models.CharField(max_length=200, blank=True, default='')

