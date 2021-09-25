from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

# app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('create_cohort/', views.cohort_form, name='cohort'),
    path('create_native/', views.native_form, name='native'),
    path('thoughts/', views.thought_form, name='thought'),
    path('display/', views.display, name='display'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
