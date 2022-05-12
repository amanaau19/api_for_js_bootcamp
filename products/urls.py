from django.urls import path
from .views import ProfessionalViewSet


urlpatterns = [
    path('products/', ProfessionalViewSet.as_view({'get': 'list'})),
    path('products/create', ProfessionalViewSet.as_view({'post': 'create'})),
    path('products/<int:pk>/', ProfessionalViewSet.as_view({'get': 'retrieve'})),
    path('products/update/<int:pk>/', ProfessionalViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('products/delete/<int:pk>/', ProfessionalViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    ]
