from django.shortcuts import render
from django.views.generic import TemplateView
from machine.models import VendingMachine, VendingMachineUser
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

# Create your views here.
class MachinePageView(TemplateView):
    template_name = 'machine-page.html'


    def get_context_data(self, **kwargs):
        context = super(MachinePageView, self).get_context_data(**kwargs)
        machine_code = kwargs.get('machine_code')
        machine = VendingMachine.objects.filter(machine_code=machine_code).first()
        if machine:
            context['inventories'] = machine.inventory_set.all()
            context['machine'] = machine
        return context


class MachineRefillPageView(TemplateView):
    template_name = 'machine-refill.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
        return super(MachineRefillPageView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MachineRefillPageView, self).get_context_data(**kwargs)
        user_machine = VendingMachineUser.objects.filter(
            user=self.request.user, is_active=True).select_related('machine')
        context['user_machine'] = user_machine
        return context

class MachineRefillDetail(TemplateView):
    template_name = "machine-refill-detail.html"

    def get(self, request, *args, **kwargs):
        from machine.models import VendingMachineUser
        machine_code = kwargs.get('machine_code')
        user_machine = VendingMachineUser.objects.filter(
            user=request.user, 
            machine__machine_code=machine_code,
            is_active=True)
        if not user_machine.exists():
            return HttpResponseForbidden()
        return super(MachineRefillDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        from inventory.models import Item 
        context = super(MachineRefillDetail, self).get_context_data(**kwargs)
        machine_code = kwargs.get('machine_code')
        machine = VendingMachine.objects.filter(machine_code=machine_code).first()
        non_existing_items = Item.objects.all().exclude(
            id__in=machine.inventory_set.values_list('item_id', flat=True)
        )
        if machine:
            context['inventories'] = machine.inventory_set.all()
            context['machine'] = machine
            context['items'] = non_existing_items
        return context
