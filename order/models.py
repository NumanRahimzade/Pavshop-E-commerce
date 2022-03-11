from core.models import AbstractModel
from django.db import models



class Order(AbstractModel):

    total = models.DecimalField('Total', decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.total)


class Basket(AbstractModel):
    sub_total = models.DecimalField('Sub-Total', decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.sub_total)


class BasketItem(AbstractModel):
    price = models.DecimalField('Price', decimal_places=2, max_digits=10)
    sub_total = models.DecimalField('Sub-Total', decimal_places=2, max_digits=10)
    count = models.IntegerField('Count')

    def __str__(self):
        return str(self.sub_total)