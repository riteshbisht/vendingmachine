from django.db import models
from machine.models import VendingMachine
# Create your models here.
from util.models import AbstractAutoDate
from user.models import BuyUser


class Item(AbstractAutoDate, models.Model):
	item_name = models.CharField(max_length=50)
	item_code = models.CharField(max_length=10, unique=True)
	item_price = models.DecimalField(
		max_digits=8, decimal_places=2,
		default=0
	)

	def __str__(self):
		return self.item_name


class Inventory(AbstractAutoDate, models.Model):
	machine = models.ForeignKey(
		VendingMachine,
		on_delete=models.PROTECT
	)
	item = models.ForeignKey(
		'Item',
		on_delete = models.PROTECT,
		related_name='items'
	)
	curr_count = models.PositiveIntegerField(default=0)


class VendingHistory(AbstractAutoDate, models.Model):
	vending_machine = models.ForeignKey(
		VendingMachine,
		on_delete = models.PROTECT,
	)
	item = models.ForeignKey(
		Item,
		on_delete = models.PROTECT,
		related_name='item_purchased'
	)
	buy_user = models.ForeignKey(
		BuyUser,
		on_delete = models.PROTECT
	)

	def __str__(self):
		return '{} - {} - {}'.format(self.vending_machine, self.item, self.buy_user)
