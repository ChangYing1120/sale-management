from django.contrib import admin
from manager.models import Customer, Salesman, TechnicalLead

# Register your models here.
admin.site.register(Customer)
admin.site.register(Salesman)
admin.site.register(TechnicalLead)
