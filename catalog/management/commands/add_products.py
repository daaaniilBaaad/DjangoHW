from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from unicodedata import category


# class Command(BaseCommand):
#     help = 'Add test products to the database'
#
#     def handle(self, *args, **options):
#         category = Category.objects.create(id=1, name='Category Test')
#
#         products = [
#             {'name': 'Product Test 1', 'price': 1000, 'category': category},
#             {'name': 'Product Test 2', 'price': 2000, 'category': category},
#         ]
#
#         from product_data in products:
#             products, created =
#

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Test category')  # type(category)

        products = [
            {'name': 'Test product 1',
             'image': '', 'price': 100, 'category': category},
            {'name': 'Test product 2',
             'price': 200, 'category': category}
        ]
        for product_in_data in products:
            product, created = Product.objects.get_or_create(**product_in_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added test product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Test product already exists: {product.name}'))