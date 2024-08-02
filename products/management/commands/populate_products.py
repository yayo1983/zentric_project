
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
        generated_names = set()
        while count < 100:
            name = fake.word().capitalize()
            if name in generated_names:
                continue  # If the name was already generated, skip it and generate another one
            description = fake.text()
            user = User.objects.order_by('?').first()
            result = Product.objects.create(
                user=user,
                name=name,
                description=description,
                price=round(random.uniform(10.0, 1000.0), 2)
            )
            count += 1
            generated_names.add(name) 
            print("Register", count, result)
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with products'))
