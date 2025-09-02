from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    """
    This is a class to define posts for blog app
    """
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    # todo: set upload to
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL,
                                 null=True, related_name="posts")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_snippet(self):
        return f"{self.content[:30]}..."

    def get_absolute_api_url(self):
        return reverse('blog:api-v1:post-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    """
    This is a class to define post category for blog app
    """
    name = models.CharField(max_length=250)
    parent = models.ForeignKey("Category", on_delete=models.SET_NULL,
                               null=True, blank=True, related_name="sub_categories")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name
