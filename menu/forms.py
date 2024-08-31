# menu/forms.py
from django import forms
from .models import Admin, Parent, Carinderia, School, Student

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'

class CarinderiaForm(forms.ModelForm):
    class Meta:
        model = Carinderia
        fields = '__all__'

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'