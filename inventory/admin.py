from django.contrib import admin

from .models import Item, Inventory, VendingHistory

class ItemAdmin(admin.ModelAdmin):
    pass

class InventoryAdmin(admin.ModelAdmin):
    pass

class VendingHistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(VendingHistory, VendingHistoryAdmin)

