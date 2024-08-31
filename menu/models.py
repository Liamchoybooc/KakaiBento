# menu/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class AdminManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class Admin(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AdminManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

# Parent Model
class Parent(models.Model):
    PARENT_ID = models.AutoField(primary_key=True)
    PARENT_FNAME = models.CharField(max_length=50)
    PARENT_LNAME = models.CharField(max_length=50)
    PARENT_DOB = models.DateField()
    PARENT_PHONE = models.CharField(max_length=15)
    PARENT_ADDRESS = models.CharField(max_length=100)
    PARENT_EMAIL = models.EmailField(max_length=50)
    PARENT_USERNAME = models.CharField(max_length=50)
    PARENT_PASSWORD = models.CharField(max_length=50)
    PARENT_ACTIVE = models.BooleanField(default=True)
    PARENT_DATECREATED = models.DateField(auto_now_add=True)
    PARENT_PROFILE = models.ImageField(upload_to='parent_profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.PARENT_FNAME} {self.PARENT_LNAME}"


# Student Model
class Student(models.Model):
    STUD_ID = models.AutoField(primary_key=True)
    STUD_FNAME = models.CharField(max_length=50)
    STUD_LNAME = models.CharField(max_length=50)
    STUD_GRADELVL = models.IntegerField()
    STUD_BIRTHDATE = models.DateField()
    STUD_SECTION = models.CharField(max_length=50)
    STUD_STUDID = models.IntegerField()
    STUD_ADDRESS = models.CharField(max_length=100)
    STUD_PHONE = models.CharField(max_length=15)
    STUD_ACTIVE = models.BooleanField(default=True)
    STUD_DATECREATED = models.DateTimeField(auto_now_add=True)
    STUD_PROFILE = models.ImageField(upload_to='student_profiles/', blank=True, null=True)
    PARENT = models.ForeignKey(Parent, on_delete=models.CASCADE)
    SCHOOL = models.ForeignKey('School', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.STUD_FNAME} {self.STUD_LNAME}"


# Carinderia Model
class Carinderia(models.Model):
    CARIN_ID = models.AutoField(primary_key=True)
    CARIN_NAME = models.CharField(max_length=50)
    CARIN_ADDRESS = models.CharField(max_length=50)
    CARIN_PHONE = models.CharField(max_length=50)
    CARIN_USERNAME = models.CharField(max_length=50)
    CARIN_PASSWORD = models.CharField(max_length=50)
    CARIN_EMAIL = models.EmailField(max_length=50)
    CARIN_IMG_CERT = models.ImageField(upload_to='carinderia/certificates/', blank=True, null=True)
    CARIN_IMG_ID = models.ImageField(upload_to='carinderia/ids/', blank=True, null=True)
    CARIN_IMG_LOC = models.ImageField(upload_to='carinderia/locations/', blank=True, null=True)
    CARIN_IMG_KIT1 = models.ImageField(upload_to='carinderia/kitchen1/', blank=True, null=True)
    CARIN_IMG_KIT2 = models.ImageField(upload_to='carinderia/kitchen2/', blank=True, null=True)
    CARIN_ACTIVE = models.BooleanField(default=True)
    CARIN_DATECREATED = models.DateField(auto_now_add=True)
    CARIN_LOGO = models.ImageField(upload_to='carinderia/logos/', blank=True, null=True)

    def __str__(self):
        return self.CARIN_NAME


# Food/Menu Model
class Menu(models.Model):
    MENU_ID = models.AutoField(primary_key=True)
    MENU_NAME = models.CharField(max_length=50)
    MENU_DESCRIPT = models.CharField(max_length=250)
    MENU_PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    MENU_CALORIE = models.DecimalField(max_digits=10, decimal_places=2)
    MENU_CARBS = models.DecimalField(max_digits=10, decimal_places=2)
    MENU_PROTEIN = models.DecimalField(max_digits=10, decimal_places=2)
    MENU_FATS = models.DecimalField(max_digits=10, decimal_places=2)
    MENU_TYPE = models.CharField(max_length=50)
    MENU_MEALTYPE = models.CharField(max_length=50)
    CARINDERIA = models.ForeignKey(Carinderia, on_delete=models.CASCADE)

    def __str__(self):
        return self.MENU_NAME


# School Model
class School(models.Model):
    SCHOOL_ID = models.AutoField(primary_key=True)
    SCHOOL_NAME = models.CharField(max_length=50)
    SCHOOL_ADDRESS = models.CharField(max_length=50)
    SCHOOL_PHONE = models.CharField(max_length=15)
    SCHOOL_EMAIL = models.EmailField(max_length=50)
    SCHOOL_DATECREATED = models.DateField(auto_now_add=True)
    SCHOOL_ACTIVE = models.BooleanField(default=True)

    def __str__(self):
        return self.SCHOOL_NAME

# School Carinderia Model
class SchoolCarinderia(models.Model):
    SCHCARIN_ID = models.AutoField(primary_key=True)
    SCHCARIN_NAME = models.CharField(max_length=50)
    CARIN_ID = models.ForeignKey(Carinderia, on_delete=models.CASCADE)
    SCHOOL_ID = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.SCHCARIN_NAME

# Student Survey Model
class StudentSurvey(models.Model):
    SS_ID = models.AutoField(primary_key=True)
    SS_AGE = models.IntegerField()
    SS_WEIGHT = models.FloatField()
    SS_HEIGHT = models.FloatField()
    SS_BMI = models.FloatField()
    SS_SEX = models.CharField(max_length=50)
    SS_ALLERGENS = models.CharField(max_length=50)
    SS_FOODPREF = models.CharField(max_length=50)
    SS_DIETARY = models.CharField(max_length=50)
    SS_ACTLVL = models.CharField(max_length=50)
    STUD_ID = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Survey of {self.STUD_ID}"

# Allergen Model
class Allergen(models.Model):
    ALRGN_ID = models.AutoField(primary_key=True)
    ALRGN_TYPE = models.CharField(max_length=50)
    ALRGN_NAME = models.CharField(max_length=50)
    SS_ID = models.ForeignKey(StudentSurvey, on_delete=models.CASCADE)

    def __str__(self):
        return self.ALRGN_NAME

# Carinderia Verification Model
class CarinderiaVerification(models.Model):
    VCARIN_ID = models.AutoField(primary_key=True)
    VCARIN_STATUS = models.CharField(max_length=50)
    CARIN_ID = models.ForeignKey(Carinderia, on_delete=models.CASCADE)

    def __str__(self):
        return f"Verification of {self.CARIN_ID}"

# Ingredient Model
class Ingredient(models.Model):
    ING_ID = models.AutoField(primary_key=True)
    ING_NAME = models.CharField(max_length=50)
    ING_TYPE = models.CharField(max_length=50)
    MENU_ID = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.ING_NAME

# Grade Level Model
class GradeLevel(models.Model):
    GRDL_ID = models.AutoField(primary_key=True)
    GRDL_GRADELVL = models.CharField(max_length=50)
    SCHOOL_ID = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.GRDL_GRADELVL

# Grade Section Model
class GradeSection(models.Model):
    GRDS_ID = models.AutoField(primary_key=True)
    GRDS_STUDID = models.IntegerField()
    GRDS_FNAME = models.CharField(max_length=50)
    GRDS_LNAME = models.CharField(max_length=50)
    GRDL_ID = models.ForeignKey(GradeLevel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.GRDS_FNAME} {self.GRDS_LNAME}"
    
class MealPlan(models.Model):
    MPLAN_ID = models.AutoField(primary_key=True)
    MPLAN_MEALTYPE = models.CharField(max_length=50)
    MPLAN_TOTALPRICE = models.FloatField()
    MPLAN_STATUS = models.CharField(max_length=50)
    STUD_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    CARIN_ID = models.ForeignKey(Carinderia, on_delete=models.CASCADE)

    def __str__(self):
        return f"Meal Plan for {self.STUD_ID}"

class Meal(models.Model):
    MEAL_ID = models.AutoField(primary_key=True)
    MEAL_DAY = models.CharField(max_length=50)
    MEAL_DATE = models.DateField()
    MEAL_SUBTOTAL = models.FloatField()
    MEAL_DLVRSTATUS = models.CharField(max_length=50)
    MPLAN_ID = models.ForeignKey(MealPlan, on_delete=models.CASCADE)

    def __str__(self):
        return f"Meal on {self.MEAL_DAY}"

class Dish(models.Model):
    DISH_ID = models.AutoField(primary_key=True)
    DISH_NAME = models.CharField(max_length=50)
    DISH_PRICE = models.FloatField()
    MEAL_ID = models.ForeignKey(Meal, on_delete=models.CASCADE)
    MENU_ID = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.DISH_NAME

class Payment(models.Model):
    PAY_ID = models.AutoField(primary_key=True)
    PAY_STATUS = models.CharField(max_length=50)
    PAY_DATESENT = models.DateTimeField()
    PAY_DATECONFIRMED = models.DateTimeField()
    PAY_TYPE = models.CharField(max_length=50)
    MPLAN_ID = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Payment {self.PAY_ID}"

class Receipt(models.Model):
    REC_ID = models.AutoField(primary_key=True)
    REC_REF = models.IntegerField()
    REC_TOTAL = models.FloatField()
    REC_DATE = models.DateTimeField()
    PAY_ID = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receipt {self.REC_REF}"

class Delivery(models.Model):
    DEL_ID = models.AutoField(primary_key=True)
    DEL_STATUS = models.CharField(max_length=50)
    DEL_DAY = models.CharField(max_length=50)
    DEL_DATE = models.DateTimeField()
    MEAL_ID = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Delivery on {self.DEL_DAY}"

class Cancellation(models.Model):
    CANC_ID = models.AutoField(primary_key=True)
    CANC_STATUS = models.CharField(max_length=50)
    CANC_REASON = models.CharField(max_length=50)
    CANC_TYPE = models.CharField(max_length=50)
    CANC_DATESENT = models.DateTimeField()
    CANC_DATECONFIRMED = models.DateTimeField()
    CANC_TOTALREFUND = models.FloatField()
    CANC_TYPE = models.CharField(max_length=50)
    MEAL_ID = models.ForeignKey(Meal, on_delete=models.CASCADE)
    MPLAN_ID = models.ForeignKey(MealPlan, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cancellation {self.CANC_STATUS}"

class Income(models.Model):
    INC_ID = models.AutoField(primary_key=True)
    INC_TOTAL = models.FloatField()
    INC_CARIN = models.FloatField()
    INC_SCHOOL = models.FloatField()
    INC_ADMIN = models.FloatField()
    MEAL_ID = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Income {self.INC_TOTAL}"

class CancellationReceipt(models.Model):
    CANCREC_ID = models.AutoField(primary_key=True)
    CANCREC_REF = models.IntegerField()
    CANCREC_TOTAL = models.FloatField()
    CANCREC_DATE = models.DateTimeField()
    CANC_ID = models.ForeignKey(Cancellation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cancellation Receipt {self.CANCREC_REF}"
