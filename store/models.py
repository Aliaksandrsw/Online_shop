from django.contrib.auth import get_user_model
from django.db import models
from users.models import User


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)


class ProductCategory(models.Model):
    name = models.CharField(max_length=129)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=1)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-quantity']
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'


class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'Корзина для {self.user.username} Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    @classmethod
    def create_or_update(cls, product_id, user):
        baskets = Basket.objects.filter(user=user, product_id=product_id)

        if not baskets.exists():
            obj = Basket.objects.create(user=user, product_id=product_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_crated = False
            return basket, is_crated
