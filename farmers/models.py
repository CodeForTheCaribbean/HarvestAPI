from django.db import models

class Farmer(models.Model):

    farmer_idx = models.IntegerField(max_length=6)
    farmer_id =  models.CharField(max_length=100, blank=False, default='', primary_key=True)
    first_name = models.CharField(max_length=100, null=True, default='')
    last_name = models.CharField(max_length=100, null=True, default='')
    alias = models.CharField(max_length=100, null=True, default='')
    res_address = models.CharField(max_length=200, null=True, default='')
    res_parish = models.CharField(max_length=20, null=True, default='')
    tel_number = models.CharField(max_length=20, null=True, default='')
    cell_number = models.CharField(max_length=20, null=True, default='')
    verified_status = models.CharField(max_length=3, null=True, default='')
    dob = models.DateTimeField()
#    reg_date = models.DateTimeField()
    agri_activity = models.CharField(max_length=150, null=True, default='')
    owner = models.ForeignKey('auth.User', related_name='farmers', default=1)
#    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('dob',)

class Receipt(models.Model):
    farmer_idx = models.CharField(max_length=100)
    receipt_no =  models.CharField(max_length=100, null=False, default='')
    rec_range1 = models.CharField(max_length=100, null=True, default='')
    rec_range2 = models.CharField(max_length=100, null=True, default='')
    investigation_status = models.CharField(max_length=100, null=True, default='')
    remarks = models.CharField(max_length=200, null=True, default='')
    farmer = models.ForeignKey(Farmer, related_name='receipts')

    class Meta:
        unique_together = ('farmer', 'farmer_idx')

    def __unicode__(self):
        return 'rec_no: %s' % (self.receipt_no)
