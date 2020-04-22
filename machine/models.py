from django.db import models
from .choices import CITY, COUNTRY
from util.models import AbstractAutoDate
from user.models import User, BuyUser
from django.db.models import F

class VendingMachine(AbstractAutoDate, models.Model):
    machine_name = models.CharField(max_length=50)
    machine_code = models.CharField(max_length=40, unique=True)
    address = models.CharField(max_length=255)
    city = models.IntegerField(choices=CITY)
    country = models.IntegerField(choices=COUNTRY)
    machine_pass_code = models.CharField(max_length=255)
    max_items = models.PositiveIntegerField()

    def belongs_item(self, item_code):
        return self.inventory_set.filter(item__item_code=item_code).exists()
    
    @property
    def can_add_more_items(self):
        return self.get_total_items_count() < self.max_items

    def has_item(self, item_code):
        return self.inventory_set.filter(item__item_code=item_code, curr_count__gt= 0).exists()

    def get_item(self, item_code):
        temp = self.inventory_set.filter(item__item_code=item_code).first()
        if temp:
            return temp.item
        return None

    def get_item_inventory(self, item_code):
        item_inventory = self.inventory_set.filter(item__item_code=item_code).first()
        if item_inventory:
            return item_inventory
        return None

    def get_total_items_count(self):
        return sum(self.inventory_set.all().values_list('curr_count', flat=True))

    def can_add_items(self, value):
        total_existing_items = self.get_total_items_count()
        return total_existing_items + value <= self.max_items

    def add_item(self, item_code, value):
        from inventory.models import Item
        if self.can_add_items(value):
            item = Item.objects.get(item_code=item_code)
            self.inventory_set.create(item=item, curr_count=value)

    def update_items(self, item_code, value):
        if self.can_add_items(value):
            item_inventory = self.get_item_inventory(item_code)
            item_inventory.curr_count = F('curr_count') + value 
            item_inventory.save()

  

    def reduce_one_item(self, item_code):
        if self.has_item(item_code):
            item_inventory = self.inventory_set.filter(item__item_code=item_code).first()
            item_inventory.curr_count = F('curr_count') - 1
            item_inventory.save()

    def create_record(self, item_code, mobile):
        from inventory.models import VendingHistory
        buy_user, created = BuyUser.objects.get_or_create(mobile_number=mobile)
        VendingHistory.objects.create(
            vending_machine=self,
            item=self.get_item(item_code),
            buy_user=buy_user
        )

    def __str__(self):
        return self.machine_name


class VendingMachineUser(AbstractAutoDate, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_vending_admin = models.BooleanField(default=False)
