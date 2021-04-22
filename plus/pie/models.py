from django.db import models

PAYMENT_MODE = (('chegue', 'chegue'),
                ('card', 'card'),
                ('cash', 'cash'),
                ('online', 'online'),
                ('draft', 'draft')

                )

BUCKET = (('<D', '<D'),
          ('D', 'D'),
          ('>D', '>D'),
          )
REGION = (('R1', 'R1'),
          ('R2', 'R2'),
          ('R3', 'R3'),
          )
DIVISION = (('D1', 'D1'),
            ('D2', 'D2'),
            ('D3', 'D3'),
            ('D4', 'D4'),)


class Showchart(models.Model):
    customer_id = models.IntegerField(null=True)
    region = models.CharField(choices=REGION,null=True, max_length=2)
    divison = models.CharField(choices=DIVISION,null=True, max_length=3)
    month = models.CharField(max_length=10, null=True)
    year = models.IntegerField(null=True)
    payment = models.CharField(null=True, max_length=4)
    bucket = models.CharField(max_length=3, null=True, choices=BUCKET)
    payment_mode = models.CharField(max_length=20, null=True, choices=PAYMENT_MODE)

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}-{}-{}".format(self.customer_id, self.region, self.divison, self.month, self.year,
                                                self.payment, self.bucket, self.payment_mode)
