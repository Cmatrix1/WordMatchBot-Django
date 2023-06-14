from django.contrib import admin
from .models import Condition, RuleSet, MessageResponse


class ConditionInline(admin.TabularInline):
    model = Condition
    extra = 1


class RuleSetInline(admin.StackedInline):
    model = RuleSet
    extra = 1


@admin.register(MessageResponse)
class MessageResponseAdmin(admin.ModelAdmin):

    list_display = ['response']


@admin.register(RuleSet)
class RuleSetAdmin(admin.ModelAdmin):
    inlines = [
        ConditionInline,
    ]
    list_display = ['response', 'operation', 'condition_count']

    def condition_count(self, obj):
        return obj.conditions.count()

    condition_count.short_description = 'تعداد شرط های مشخص شده'


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ['keywords', 'operation', 'ruleset']

