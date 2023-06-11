from django.contrib import admin
from .models import Condition, MessageResponse


class ConditionInline(admin.TabularInline):
    model = Condition
    extra = 0


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'response')
    inlines = [ConditionInline]


class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'keywords', 'operation', 'response')
    list_filter = ('response',)
    search_fields = ('keywords',)


admin.site.register(MessageResponse, ResponseAdmin)
admin.site.register(Condition, ConditionAdmin)
