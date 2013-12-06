from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


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

#def save(self, *args, **kwargs):
#    """
#    Use the `pygments` library to create a highlighted HTML
#    representation of the code farmer.
#    """
#    lexer = get_lexer_by_name(self.language)
#    linenos = self.linenos and 'table' or False
#    options = self.title and {'title': self.title} or {}
#    formatter = HtmlFormatter(style=self.style, linenos=linenos,
#                              full=True, **options)
#    self.highlighted = highlight(self.code, lexer, formatter)
#    super(Farmer, self).save(*args, **kwargs)

class Receipt(models.Model):
    farmer_idx = models.IntegerField(max_length=6)
    receipt_no =  models.CharField(max_length=12, blank=False, default='')
    rec_range1 = models.CharField(max_length=100, blank=True, default='')
    rec_range2 = models.CharField(max_length=100, blank=True, default='')
    investigation_status = models.CharField(max_length=100, blank=True, default='')
    remarks = models.CharField(max_length=200, blank=True, default='')

