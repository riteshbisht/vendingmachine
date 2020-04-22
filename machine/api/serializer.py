
from rest_framework import serializers
from machine.models import VendingMachine
from inventory.models import Item 

class MachineBuySerializer(serializers.Serializer):
    item_code = serializers.CharField()
    machine_code = serializers.CharField()
    mobile = serializers.CharField()

    def validate(self, data):
        machine_code = data.get('machine_code')
        item_code = data.get('item_code')
        machine = VendingMachine.objects.get(machine_code=machine_code)
        
        if not machine or not machine.has_item(item_code):
            raise serializers.ValidationError(
                'Either machine code does exist or item does not belong to machine or machine has 0 items'
            )
        return data

    def validate_mobile(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError(
                'Please enter mobile number with 10 digits'
            )
        return value


class MachineAddSerializer(serializers.Serializer):
    item_code = serializers.CharField()
    machine_code = serializers.CharField()
    amount_to_add = serializers.IntegerField()

    def validate_item_code(self, value):
        item_code = value
        if not Item.objects.filter(item_code=item_code).exists():
            raise serializers.ValidationError(
                'No Item Exists'
            )
        return value 

    def validate_machine_code(self, value):
        machine_code =  value
        if not VendingMachine.objects.filter(machine_code=machine_code).exists():
            raise serializers.ValidationError(
                'No Machine Exists'
            )
        return value

    def validate_amount_to_add(self, value):
        if value <= 0:
            raise serializers.ValidationError('Amount should be greater than 0.')
        return value

    def validate(self, data):
        machine_code = data.get('machine_code')
        item_code = data.get('item_code')
        amount_to_add = data.get('amount_to_add')
        machine = VendingMachine.objects.filter(machine_code=machine_code).first()

        if machine.belongs_item(item_code):
            raise serializers.ValidationError(
                'Item Already exist'
            ) 
        if not machine.can_add_items(amount_to_add):
            raise serializers.ValidationError(
                'Cannot Add More than {} Items.Currently has {} items'.format(machine.max_items, machine.get_total_items_count())
            ) 
        return data


class UpdateMachineSerializer(MachineAddSerializer):
    
    def validate(self, data):
        machine_code = data.get('machine_code')
        item_code = data.get('item_code')
        amount_to_add = data.get('amount_to_add')
        machine = VendingMachine.objects.filter(machine_code=machine_code).first()

        if not machine.can_add_items(amount_to_add):
            raise serializers.ValidationError(
                'Cannot Add More than {} Items.Currently has {} items'.format(machine.max_items, machine.get_total_items_count())
            ) 
        return data
