from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('create_cohort/', views.cohort_form, name='cohort'),
    path('create_native/', views.native_form, name='native')
]
