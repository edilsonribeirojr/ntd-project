from django.contrib import admin
from django.urls import path, include
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import', views.import_data_from_endpoint, name='import_data_from_endpoint'),
    path('', include('crud.urls')),
]
