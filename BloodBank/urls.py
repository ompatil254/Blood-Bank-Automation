from django.urls import path
from . import views


urlpatterns =[
    path('', views.home,name='home'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('register/<int:group_id>/', views.register, name="register"),
    path('Admin_register/', views.Admin_register, name="Admin_register"),
    path('CreateDrive/', views.CreateDrive, name="CreateDrive"),

    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('drive/<str:drive_name>/', views.drive_details, name='drive_dets'),
    path('rfid_val/', views.rfid_val, name='rfid_val'),
    path('main_storage/', views.main_storage, name="main_storage"),
    path('transfer/<str:drive_name>/', views.transfer_to_main, name='transfer_to_main')

]


