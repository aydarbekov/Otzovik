from django.conf import settings
from django.db import models


CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория')
    description = models.CharField(null=True, blank=True, max_length=300, verbose_name='Описание')
    picture = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                             verbose_name='Пользователь', related_name='reviews')
    product = models.ForeignKey('Product', null=True, blank=True, related_name='reviews', on_delete=models.SET_NULL,
                                verbose_name='Товар')
    review = models.CharField(max_length=300, verbose_name='Отзыв')
    point = models.FloatField(verbose_name='Оценка')


    def __str__(self):
        return "{} / {} - {}".format(self.product, self.user, self.point)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'