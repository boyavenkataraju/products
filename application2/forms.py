from application2.models import Employees,Registration
from django.forms import ModelForm

class EmployeesForm(ModelForm):
    class Meta:
        model=Employees
        fields="__all__"

class RegistrationForm(ModelForm):
    class Meta:
        model=Registration
        fields="__all__"
        