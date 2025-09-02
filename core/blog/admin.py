from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'status', 'category',
                    'created_date', 'published_date')

    fieldsets = (
        (_('Post Edit'), {"fields": (
            "author",
            "image",
            "title",
            "content",
            "status",
            "category",
        )}),
        (_("Important dates"), {"fields": ("published_date", "created_date", "updated_date")}),
    )

    readonly_fields = ("created_date", "updated_date")

    add_fieldsets = (
        (
            _('Add Profile'),
            {
                "classes": ("wide",),
                "fields": (
                    "author",
                    "image",
                    "title",
                    "content",
                    "status",
                    "category",
                    "published_date"
                )
            },
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'parent')

    fieldsets = (
        (_('Category Edit'), {"fields": (
            "name",
            "parent",
        )}),
        (_("Important dates"), {"fields": ("created_date", "updated_date")}),
    )

    readonly_fields = ("created_date", "updated_date")

    add_fieldsets = (
        (
            _('Add Profile'),
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "parent",
                )
            },
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
