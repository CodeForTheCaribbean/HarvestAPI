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
        # dirty IF
        if self.alias and self.cell_number:
            return ' Name - %s "%s" %s Cell %s' % ( self.first_name, self.alias, self.last_name, self.cell_number)
        elif self.cell_number:
            return ' Name - %s %s Cell %s' % ( self.first_name, self.last_name, self.cell_number)
        else:
            return ' Name - %s %s' % ( self.first_name, self.last_name)

class Receipt(models.Model):
#    farmer_idx = models.CharField(max_length=100, null=False, default='')
    receipt_no =  models.CharField(max_length=100, null=False, default='', primary_key=True)
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

class Farm(models.Model):

#    farmer_id = models.CharField(max_length=100, null=False, default='')
    farmer_idx = models.CharField(max_length=100, null=False, default='')
    farm_address = models.CharField(max_length=255, default='')
    farm_id = models.CharField(max_length=100, default='', primary_key=True)
    parish = models.CharField(max_length=30, default='')
    district = models.CharField(max_length=50, default='')
    extension = models.CharField(max_length=50, default='')
    farm_size = models.CharField(max_length=50, default='', null=True)
    lat = models.CharField(max_length=50, default='', null=True)
    long = models.CharField(max_length=50, default='', null=True)
    farm_status = models.CharField(max_length=50, default='')
    farmer = models.ForeignKey(Farmer)

    class Meta:
        ordering = ('district',)

    def __unicode__(self):
        return 'Farm Info - Parish %s Address %s Farm Status %s' % (self.parish, self.farm_address, self.farm_status)

class Crop(models.Model):

    crop_name = models.CharField(max_length=100, default='')
    common_name = models.CharField(max_length=30, default='', null=True)
    estimated_vol = models.CharField(max_length=50, default='', null=True)
    variety = models.CharField(max_length=50, default='', null=True)
    plant_date = models.CharField(max_length=50, default='', null=True)
    count = models.CharField(max_length=50, default='', null=True)
    area = models.CharField(max_length=50, default='', null=True)
    status = models.CharField(max_length=50, default='', null=True)
    exp_date = models.CharField(max_length=50, default='', null=True)
    farm = models.ForeignKey(Farm)

    class Meta:
        ordering = ('crop_name',)


class Livestock(models.Model):

    livestock_name = models.CharField(max_length=100, default='')
    count = models.CharField(max_length=50, default='', null=True)
    capacity = models.CharField(max_length=50, default='', null=True)
    stage = models.CharField(max_length=50, default='', null=True)
    farm = models.ForeignKey(Farm)

    class Meta:
        ordering = ('livestock_name',)


