from django.db import models
from apps.employees.models import Employees
from apps.repository.models import Repository


class Lend(models.Model):

    NORMAL = 'BT'
    INSURANCE = 'BH'
    CONDITION = [
        (NORMAL, 'NORMAL'),
        (INSURANCE, 'INSURANCE')
    ]

    lend_id = models.CharField(db_column='LEND_ID', primary_key=True, max_length=4)  # Field name made lowercase.
    stt = models.IntegerField(db_column='STT')  # Field name made lowercase.
    device_code = models.CharField(db_column='DEVICE_CODE', max_length=45)  # Field name made lowercase.
    rent_time = models.DateField(db_column='RENT_TIME', blank=True, null=True)  # Field name made lowercase.
    pay_time = models.DateField(db_column='PAY_TIME', blank=True, null=True)  # Field name made lowercase.
    describe = models.CharField(db_column='DESCRIBE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    insurance_start = models.DateField(db_column='INSURANCE_START', blank=True, null=True)  # Field name made lowercase.
    insurance_end = models.DateField(db_column='INSURANCE_END', blank=True, null=True)  # Field name made lowercase.
    warranty = models.CharField(db_column='WARRANTY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    condition = models.CharField(db_column='CONDITION', choices=CONDITION, max_length=45, blank=True, null=True)  # Field name made lowercase.
    id = models.ForeignKey(Employees, related_name='lend', on_delete=models.CASCADE, db_column='ID')  # Field name made lowercase.
    product = models.ForeignKey(Repository, models.DO_NOTHING, db_column='PRODUCT_ID')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lend'
