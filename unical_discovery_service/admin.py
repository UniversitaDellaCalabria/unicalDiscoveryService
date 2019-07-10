from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import EntityType, Entity


@admin.register(EntityType)
class EntityTypeAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'type')


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'type',
                    'entity_id',
                    'get_logo',
                    'updated',
                    'is_active')
    readonly_fields = ('get_logo',)
    list_editable = ('is_active',)

    def get_logo(self, obj):
        return  mark_safe(('<img src="{}" '
                           'style="max-width: 180px;"/>').format(obj.logo))
    get_logo.short_description = 'logo'
