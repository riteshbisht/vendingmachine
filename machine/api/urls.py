
from django.urls import path
from .views import AddMachineItem, BuyMachineItem, UpdateMachineItem


urlpatterns = [
    path('<slug:machine_code>/add/', AddMachineItem.as_view(), name='add-item'),
    path('<slug:machine_code>/buy/', BuyMachineItem.as_view(), name='buy-item'),
    path('<slug:machine_code>/update/', UpdateMachineItem.as_view(), name='update-item'),

]
