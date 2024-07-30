from django.contrib import admin
from .infrastructure.models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'message', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at', 'recipient')
    search_fields = ('message', 'recipient__username')
    readonly_fields = ('created_at',)



admin.site.register(Notification, NotificationAdmin)

