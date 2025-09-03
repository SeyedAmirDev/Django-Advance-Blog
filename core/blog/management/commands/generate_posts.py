import random

from faker import Faker

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

from blog.models import Post, Category
from accounts.models import Profile

class Command(BaseCommand):
    help = 'Generate fake posts'

    def handle(self, *args, **options):
        fake = Faker()

        categories = Category.objects.all()
        try:
            author = Profile.objects.filter(user__is_superuser=True).select_related("user").first()
        except Profile.DoesNotExist:
            raise CommandError("No profile for superuser found. Please create a superuser first.")
            # generate posts
        for _ in range(20):
            title = fake.unique.word()
            content = fake.paragraph(nb_sentences=20)
            status = fake.boolean()
            published_date = fake.date_time_this_year()
            category = random.choice(categories)

            Post.objects.get_or_create(
                author=author,
                title=title,
                content=content,
                status=status,
                published_date=published_date,
                category=category,
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully generated 20 fake categories'))
