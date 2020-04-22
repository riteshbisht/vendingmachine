from django.contrib import admin

from .models import VendingMachine, VendingMachineUser

class VendingMachineAdmin(admin.ModelAdmin):
    pass

class VendingMachineUserAdmin(admin.ModelAdmin):
	pass


admin.site.register(VendingMachine, VendingMachineAdmin)
admin.site.register(VendingMachineUser, VendingMachineUserAdmin)

