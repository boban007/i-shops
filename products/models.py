from django.db import models


CONTAINER_TYPE = (
    ('bottle', 'bottle'),
    ('cap', 'cap'),
    ('cream', 'cream'),
    ('inhaler', 'inhaler'),
    ('pack', 'pack'),
    ('pill', 'pill'),
    ('sachet', 'sachet'),
    ('spray', 'spray'),
    ('tab', 'tab'),
    ('tablet', 'tablet'),
    ('tube', 'tube'),
)

class Products(models.Model):
    named_id = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField()
    is_brand = models.BooleanField()
    is_sale = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    container_type = models.CharField(max_length=10, choices=CONTAINER_TYPE)
    per_item = models.DecimalField(max_digits=8, decimal_places=4)

    def __str__(self):
        return self.named_id

    class Meta:
        verbose_name = 'Producs'
        verbose_name_plural = 'Products'

class ProductCategory(models.Model):
    product_id = models.ForeignKey('Products', on_delete=models.CASCADE)
    category_id = models.ForeignKey('category.Category', on_delete=models.CASCADE)

class ProductGeneric(models.Model):
    product_id = models.ForeignKey('Products', on_delete=models.CASCADE)
    generic_id = models.ForeignKey('generic_name.GenericName', on_delete=models.CASCADE)

