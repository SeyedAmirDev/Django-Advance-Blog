import random

from faker import Faker

from django.core.management.base import BaseCommand

from blog.models import Category


class Command(BaseCommand):
    help = 'Generate fake categories'

    def handle(self, *args, **options):
        fake = Faker()

        categories = []

        # generate parent categories
        for _ in range(5):
            name = fake.unique.word()
            category, _ = Category.objects.get_or_create(name=name, parent=None)
            categories.append(category)

        # generate categories
        for _ in range(10):
            name = fake.unique.word()
            parent = random.choice(categories)
            category, _ = Category.objects.get_or_create(name=name, parent=parent)

        self.stdout.write(self.style.SUCCESS(
            'Successfully generated 15 fake categories'))
