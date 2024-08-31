from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import firebase_admin
from firebase_admin import auth
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Admin
from .forms import AdminForm
from .serializers import *
from .models import *
from .forms import *

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Account is inactive.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'menu/admin_login.html')

def user_logout(request):
    logout(request)
    return redirect('admin_login')

def create_firebase_user(request):
    try:
        user = auth.create_user(
            email=request.POST.get('email'),
            email_verified=False,
            password=request.POST.get('password'),
            display_name=request.POST.get('display_name'),
            disabled=False
        )
        return JsonResponse({'message': 'Successfully created new user', 'uid': user.uid})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def create_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_list')  # Redirect to admin list page
    else:
        form = AdminForm()
    return render(request, 'menu/admin_form.html', {'form': form})

def admin_dashboard(request):
    return render(request, 'menu/admin_dashboard.html')
    
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class CarinderiaViewSet(viewsets.ModelViewSet):
    queryset = Carinderia.objects.all()
    serializer_class = CarinderiaSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SchoolCarinderiaViewSet(viewsets.ModelViewSet):
    queryset = SchoolCarinderia.objects.all()
    serializer_class = SchoolCarinderiaSerializer

class StudentSurveyViewSet(viewsets.ModelViewSet):
    queryset = StudentSurvey.objects.all()
    serializer_class = StudentSurveySerializer

class AllergenViewSet(viewsets.ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer

class CarinderiaVerificationViewSet(viewsets.ModelViewSet):
    queryset = CarinderiaVerification.objects.all()
    serializer_class = CarinderiaVerificationSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class GradeLevelViewSet(viewsets.ModelViewSet):
    queryset = GradeLevel.objects.all()
    serializer_class = GradeLevelSerializer

class GradeSectionViewSet(viewsets.ModelViewSet):
    queryset = GradeSection.objects.all()
    serializer_class = GradeSectionSerializer

class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class CancellationViewSet(viewsets.ModelViewSet):
    queryset = Cancellation.objects.all()
    serializer_class = CancellationSerializer

class CancellationReceiptViewSet(viewsets.ModelViewSet):
    queryset = CancellationReceipt.objects.all()
    serializer_class = CancellationReceiptSerializer

def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'menu/admin_list.html', {'admins': admins})

def update_admin(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('admin_list')  # Redirect to admin list page
    else:
        form = AdminForm(instance=admin)
    return render(request, 'menu/admin_form.html', {'form': form})

def delete_admin(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    if request.method == 'POST':
        admin.delete()
        return redirect('admin_list')  # Redirect to admin list page
    return render(request, 'menu/admin_confirm_delete.html', {'admin': admin})

# Parent Views
def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'menu/parent_list.html', {'parents': parents})

def parent_detail(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    return render(request, 'menu/parent_detail.html', {'parent': parent})

def parent_create(request):
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES)
        if form.is_valid():
            parent = form.save()
            return redirect('parent_detail', pk=parent.pk)
    else:
        form = ParentForm()
    return render(request, 'menu/parent_form.html', {'form': form})

def parent_update(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES, instance=parent)
        if form.is_valid():
            parent = form.save()
            return redirect('parent_detail', pk=parent.pk)
    else:
        form = ParentForm(instance=parent)
    return render(request, 'menu/parent_form.html', {'form': form})

def parent_delete(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    if request.method == 'POST':
        parent.delete()
        return redirect('parent_list')
    return render(request, 'menu/parent_confirm_delete.html', {'parent': parent})

# Carinderia Views
def carinderia_list(request):
    carinderias = Carinderia.objects.all()
    return render(request, 'menu/carinderia_list.html', {'carinderias': carinderias})

def carinderia_detail(request, pk):
    carinderia = get_object_or_404(Carinderia, pk=pk)
    return render(request, 'menu/carinderia_detail.html', {'carinderia': carinderia})

def carinderia_create(request):
    if request.method == 'POST':
        form = CarinderiaForm(request.POST, request.FILES)
        if form.is_valid():
            carinderia = form.save()
            return redirect('carinderia_detail', pk=carinderia.pk)
    else:
        form = CarinderiaForm()
    return render(request, 'menu/carinderia_form.html', {'form': form})

def carinderia_update(request, pk):
    carinderia = get_object_or_404(Carinderia, pk=pk)
    if request.method == 'POST':
        form = CarinderiaForm(request.POST, request.FILES, instance=carinderia)
        if form.is_valid():
            carinderia = form.save()
            return redirect('carinderia_detail', pk=carinderia.pk)
    else:
        form = CarinderiaForm(instance=carinderia)
    return render(request, 'menu/carinderia_form.html', {'form': form})

def carinderia_delete(request, pk):
    carinderia = get_object_or_404(Carinderia, pk=pk)
    if request.method == 'POST':
        carinderia.delete()
        return redirect('carinderia_list')
    return render(request, 'menu/carinderia_confirm_delete.html', {'carinderia': carinderia})

# School Views
def school_list(request):
    schools = School.objects.all()
    return render(request, 'menu/school_list.html', {'schools': schools})

def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk)
    return render(request, 'menu/school_detail.html', {'school': school})

def school_create(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            school = form.save()
            return redirect('school_detail', pk=school.pk)
    else:
        form = SchoolForm()
    return render(request, 'menu/school_form.html', {'form': form})

def school_update(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=school)
        if form.is_valid():
            school = form.save()
            return redirect('school_detail', pk=school.pk)
    else:
        form = SchoolForm(instance=school)
    return render(request, 'menu/school_form.html', {'form': form})

def school_delete(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        school.delete()
        return redirect('school_list')
    return render(request, 'menu/school_confirm_delete.html', {'school': school})

# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'menu/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'menu/student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'menu/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'menu/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'menu/student_confirm_delete.html', {'student': student})

