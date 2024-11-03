from django.contrib import admin
from django.utils.html import format_html
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_colored', 'created_at', 'updated_at', 'preview_description')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10  # số items trên mỗi trang

    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('name', 'description', 'price')
        }),
        ('Thông tin thời gian', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def price_colored(self, obj):
        if obj.price > 1000:
            color = 'red'
        elif obj.price > 500:
            color = 'orange'
        else:
            color = 'green'
        return format_html('<span style="color: {};">${}</span>', color, obj.price)

    price_colored.short_description = 'Giá'

    def preview_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description

    preview_description.short_description = 'Mô tả ngắn'

    # Tùy chỉnh actions
    actions = ['mark_as_featured']

    def mark_as_featured(self, request, queryset):
        # Giả sử bạn có trường featured trong model
        queryset.update(featured=True)

    mark_as_featured.short_description = "Đánh dấu là sản phẩm nổi bật"

    # Tùy chỉnh giao diện chi tiết
    def get_fieldsets(self, request, obj=None):
        if not obj:  # Khi tạo mới
            return (
                ('Thông tin cơ bản', {
                    'fields': ('name', 'description', 'price')
                }),
            )
        return self.fieldsets  # Khi chỉnh sửa