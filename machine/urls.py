
from django.urls import path
from .views import MachinePageView, MachineRefillPageView, MachineRefillDetail
urlpatterns = [
    path('refill/', MachineRefillPageView.as_view(), name='machine-refill'),
    path('refill/<slug:machine_code>', MachineRefillDetail.as_view(), name="machine-refill-detail"),
    path('<slug:machine_code>/', MachinePageView.as_view(), name='machine-detail')

]
