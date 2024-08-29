from django.urls import path
from crud_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)