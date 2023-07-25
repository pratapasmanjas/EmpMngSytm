from django.contrib import admin
from .models import employee,Role,Dept
# Register your models here.
admin.site.register(employee)
admin.site.register(Role)
admin.site.register(Dept)