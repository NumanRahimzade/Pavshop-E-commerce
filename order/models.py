from core.models import AbstractModel
from product.models import ProductVersion
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Order(AbstractModel):
    basket = models.OneToOneField('Basket', default='', on_delete=models.CASCADE)

    total = models.DecimalField('Total', decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.total)


class Basket(AbstractModel):
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE)

    sub_total = models.DecimalField('Sub Total', decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.sub_total)


class BasketItem(AbstractModel):
    basket = models.ForeignKey(Basket, default='', on_delete=models.CASCADE)
    productVersion = models.ForeignKey(ProductVersion, default='', on_delete=models.CASCADE, verbose_name='Product Version')

    price = models.DecimalField('Price', decimal_places=2, max_digits=10)
    sub_total = models.DecimalField('Sub-Total', decimal_places=2, max_digits=10)
    count = models.IntegerField('Count')

    def __str__(self):
        return str(self.sub_total)