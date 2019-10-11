from django.db import models
import uuid

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

MEASURE = (
    ('mcg', 'mcg'),
    ('mg', 'mg'),
    ('g', 'g'),
)

class Product(models.Model):
    named_id = models.SlugField(primary_key=True)
    is_active = models.BooleanField()
    is_brand = models.BooleanField()
    is_sale = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    container_type = models.CharField(max_length=10, choices=CONTAINER_TYPE)
    per_item = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.named_id

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductCategory(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    category_id = models.ForeignKey('category.Category', on_delete=models.CASCADE)


class ProductGeneric(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    generic_id = models.ForeignKey('generic_name.GenericName', on_delete=models.CASCADE)


def get_uid():
    return uuid.uuid4().hex[:8]


class Pack(models.Model):
    uid = models.CharField(max_length=8, editable=False, unique=True, default=get_uid)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    dosage = models.DecimalField(max_digits=6, decimal_places=2)
    measure = models.CharField(max_length=10, choices=MEASURE)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

