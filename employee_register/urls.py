from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.employee_form), #localhost
    path('list/', views.employee_list),
]