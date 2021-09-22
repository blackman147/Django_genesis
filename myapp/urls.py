from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('create_cohort/', views.cohort_form, name='cohort'),
    path('create_native/', views.native_form, name='native'),
    path('display/', views.display, name ='display'),
    path('home/', views.home, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
