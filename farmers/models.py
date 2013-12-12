from django.db import models

class Farmer(models.Model):

    farmer_idx =  models.CharField(max_length=100, blank=False, default='')
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
    agri_activity = models.CharField(max_length=150, null=True, default='')
    owner = models.ForeignKey('auth.User', related_name='farmers', default='1', null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
#    receipts = models.ForeignKey(Receipt, related_name='farmers', null=True)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return 'First Name :%s Last Name: %s ID: %s  Alias: %s ' % ( self.first_name, self.last_name, self.farmer_id, self.alias)

class Receipt(models.Model):
#    farmer_idx = models.CharField(max_length=100, null=False, default='')
    receipt_no =  models.CharField(max_length=100, null=False, default='')
    rec_range1 = models.CharField(max_length=100, null=True, default='')
    rec_range2 = models.CharField(max_length=100, null=True, default='')
    investigation_status = models.CharField(max_length=100, null=True, default='')
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
    remarks = models.CharField(max_length=200, null=True, default='')
    farmer = models.ForeignKey(Farmer)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return 'Receipt no: %s' % (self.receipt_no)


