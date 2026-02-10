'''from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__' '''

from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
       model=Employee
       fields=  '__all__'