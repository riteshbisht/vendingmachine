import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from machine.models import VendingMachine, VendingMachineUser
from inventory.models import Item
from machine.choices import COUNTRY, CITY
from user.models import User

class Command(BaseCommand):
    help = 'Displays current time'

    def get_city_val(self):
        r = random.randint(1,len(CITY)-1)
        return CITY[r][0] 

    def handle(self, *args, **kwargs):
        machine_keys = ['machine_name'
            'machine_code',
            'address', 
            'city',
            'country',
            'machine_pass_code',
            'max_items'
        ]
        items = [
                ('lays', 'lays_01', 20), ('coke', 'coke_01',40),
                ('good_day', 'goodday_01',10), ('kurkure', 'kurkure', 25)
            ]

        for item, code, price in items:
            data = {
                'item_name': item,
                'item_code': code,
                'item_price': price
            }
            Item.objects.create(**data)
        for i in range(1, 5):
            data = {
            'machine_name': 'machine_name - {}'.format(str(i)),
            'machine_code': 'machine{}'.format(str(i)),
            'address': 'random adress',
            'city': self.get_city_val(),
            'country': 1,
            'machine_pass_code': random.randint(1000, 30000),
            'max_items': random.randint(20, 40)
            }
            VendingMachine.objects.create(**data)

        user = User.objects.create(
            username='root',
            email='root@root.com',
            is_superuser=True,
            is_active=True
        )
        for machine in VendingMachine.objects.all():
            VendingMachineUser.objects.create(
                machine=machine,
                user=user,
                is_active=True,
                is_vending_admin=True
            )
        user.set_password('root')
        user.save()
