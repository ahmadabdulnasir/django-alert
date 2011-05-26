from django.contrib import admin
from models import Alert, AlertPreference

class AlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'backend', 'alert_type', 'failed', 'is_sent', 'created',)
    list_filter = ('alert_type', 'backend', 'is_sent', 'failed')
    search_fields = ('=user__username', '=user__email')

class AlertPrefAdmin(admin.ModelAdmin):
    list_display = ("user", 'alert_type', "backend", 'preference')
    list_filter = ('alert_type', 'backend', 'preference')
    search_fields = ('=user__username', '=user__email')
    

admin.site.register(Alert, AlertAdmin)
admin.site.register(AlertPreference, AlertPrefAdmin)