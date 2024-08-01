
import random
from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from products.infrastructure.models import Product


class Command(BaseCommand):
    help = 'Populate the Product model with dummy data'

    def handle(self, *args, **kwargs):
        count = 0
        fake = Faker()
        for _ in range(100):
            name = fake.word().capitalize()
            description = fake.text()
            user = User.objects.order_by('?').first()
            result = Product.objects.create(
                user=user,
                name=name,
                description=description,
                price=round(random.uniform(10.0, 1000.0), 2)
            )
            count += 1
            print("Register", count, result)
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with products'))
