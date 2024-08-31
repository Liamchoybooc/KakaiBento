from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, create_firebase_user
from .views import admin_login
from django.conf import settings
from django.conf.urls.static import static

# Define DRF router
router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'parents', views.ParentViewSet)
router.register(r'schools', views.SchoolViewSet)
router.register(r'carinderias', views.CarinderiaViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'menus', views.MenuViewSet)
router.register(r'schoolcarinderias', views.SchoolCarinderiaViewSet)
router.register(r'studentsurveys', views.StudentSurveyViewSet)
router.register(r'allergens', views.AllergenViewSet)
router.register(r'carinderiaverifications', views.CarinderiaVerificationViewSet)
router.register(r'ingredients', views.IngredientViewSet)
router.register(r'gradelevels', views.GradeLevelViewSet)
router.register(r'gradesections', views.GradeSectionViewSet)
router.register(r'mealplans', views.MealPlanViewSet)
router.register(r'meals', views.MealViewSet)
router.register(r'dishes', views.DishViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'receipts', views.ReceiptViewSet)
router.register(r'deliveries', views.DeliveryViewSet)
router.register(r'incomes', views.IncomeViewSet)
router.register(r'cancellations', views.CancellationViewSet)
router.register(r'cancellationreceipts', views.CancellationReceiptViewSet)


# Define urlpatterns
urlpatterns = [
    
    path('', views.admin_login, name='admin_login'),  # Example custom view for home page
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.user_logout, name='user_logout'),
    
    # Admin URLs
    path('admin/create/', views.create_admin, name='create_admin'),
    path('admin/<int:pk>/update/', views.update_admin, name='update_admin'),
    path('admin/<int:pk>/delete/', views.delete_admin, name='delete_admin'),
    path('admin/', views.admin_list, name='admin_list'),

    # Parent URLs
    path('parents/', views.parent_list, name='parent_list'),
    path('parents/create/', views.parent_create, name='parent_create'),
    path('parents/<int:pk>/', views.parent_detail, name='parent_detail'),
    path('parents/<int:pk>/update/', views.parent_update, name='parent_update'),
    path('parents/<int:pk>/delete/', views.parent_delete, name='parent_delete'),

    # Carinderia URLs
    path('carinderias/', views.carinderia_list, name='carinderia_list'),
    path('carinderias/create/', views.carinderia_create, name='carinderia_create'),
    path('carinderias/<int:pk>/', views.carinderia_detail, name='carinderia_detail'),
    path('carinderias/<int:pk>/update/', views.carinderia_update, name='carinderia_update'),
    path('carinderias/<int:pk>/delete/', views.carinderia_delete, name='carinderia_delete'),

    # School URLs
    path('schools/', views.school_list, name='school_list'),
    path('schools/create/', views.school_create, name='school_create'),
    path('schools/<int:pk>/', views.school_detail, name='school_detail'),
    path('schools/<int:pk>/update/', views.school_update, name='school_update'),
    path('schools/<int:pk>/delete/', views.school_delete, name='school_delete'),

    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # Include DRF router URLs
    path('api/', include(router.urls)),

    # Endpoint for creating Firebase user
    path('create_firebase_user/', create_firebase_user, name='create_firebase_user'),
]

# Add media URL configuration for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
