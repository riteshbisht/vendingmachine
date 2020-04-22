from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializer import MachineBuySerializer, MachineAddSerializer, UpdateMachineSerializer
from machine.models import VendingMachine

class BuyMachineItem(CreateAPIView):
    serializer_class = MachineBuySerializer
    authentication_classes = ()
    
    def perform_create(self, serializer):
        machine_code = serializer.data.get('machine_code')
        item_code = serializer.data.get('item_code')
        mobile = serializer.data.get('mobile')
        machine = VendingMachine.objects.get(machine_code=machine_code)
        machine.reduce_one_item(item_code)
        machine.create_record(item_code, mobile)


class AddMachineItem(CreateAPIView):
    serializer_class = MachineAddSerializer
    authentication_classes = ()

    def perform_create(self, serializer):
        machine_code = serializer.data.get('machine_code')
        item_code = serializer.data.get('item_code')
        amount_to_add = serializer.data.get('amount_to_add')
        machine = VendingMachine.objects.get(machine_code=machine_code)
        machine.add_item(item_code, amount_to_add)


class UpdateMachineItem(CreateAPIView):
    serializer_class = UpdateMachineSerializer

    def perform_create(self, serializer):
        machine_code = serializer.data.get('machine_code')
        item_code = serializer.data.get('item_code')
        amount_to_add = serializer.data.get('amount_to_add')
        machine = VendingMachine.objects.get(machine_code=machine_code)
        machine.update_items(item_code, amount_to_add)
    
