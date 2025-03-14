from django.contrib import admin

from .models import Product, Comment

# Internationalization or i18n

class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active',]
    extra = 1


# class CommentsInline(admin.StackedInline):
#     model = Comment
#     fields = ['author', 'body', 'stars', 'active',]
#


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'datetime_created', 'datetime_modified', ]

    inlines = [
        CommentsInline,
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product','author', 'body', 'stars', 'active', 'datetime_created', 'datetime_modified', ]
