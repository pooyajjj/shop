from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=225)
    desc = models.TextField(max_length=1100, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=225)
    size = models.IntegerField(null=True, blank=True)
    desc = models.TextField(max_length=1100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    img = models.ImageField()
    title = models.TextField(max_length=1100)
    slug = models.CharField(max_length=225, unique=True)
    avalibale = models.SmallIntegerField()
    have_unique_code = models.BooleanField(default=False)
    unique_code = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}, {self.unique_code}'