from django.db import models


class Showchart(models.Model):
    customer_id = models.IntegerField(null=True)
    region = models.CharField(null=True, max_length=2)
    divison = models.CharField(null=True, max_length=3)
    month = models.CharField(max_length=10, null=True)
    year = models.IntegerField(null=True)
    payment = models.CharField(null=True, max_length=4)
    bucket = models.CharField(max_length=3, null=True)
    payment_mode = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}-{}-{}".format(self.customer_id, self.region, self.divison, self.month, self.year,
                                                self.payment, self.bucket, self.payment_mode)
