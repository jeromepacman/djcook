from django.contrib import admin

from . import models


@admin.register(models.BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'username', 'first_name', 'last_name', 'joined', 'language_code')
    order_by = ('last_action_datetime',)


