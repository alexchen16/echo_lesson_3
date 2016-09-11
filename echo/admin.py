from django.contrib import admin
from .models import Node,Line,Device
# Register your models here.
class NodeAdmin(admin.ModelAdmin):
    list_display = ('node_name','node_address','node_signer','node_signtime')

class LineAdmin(admin.ModelAdmin):
    list_display = ('line_code','line_spname','line_local')

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_caption','device_vendor','device_ip')


admin.site.register(Node,NodeAdmin)
admin.site.register(Line,LineAdmin)
admin.site.register(Device,DeviceAdmin)

