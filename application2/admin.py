from django.contrib import admin
from application2.models import Employees,Registration

class EmployeesAdmin(admin.ModelAdmin):
    list_display=['Eid','Ename','Esal','Design','Company','Join_Date','Location']
admin.site.register(Employees,EmployeesAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    list_display=['First_Name','Last_Name','User_Name','Password','Email','Mobile_No']
admin.site.register(Registration,RegistrationAdmin)
