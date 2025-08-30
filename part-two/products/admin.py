from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description', 'get_tags')
    search_fields = ('name','category','description')
    list_filter = ('category',)

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'
