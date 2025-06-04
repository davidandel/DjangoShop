from django.urls import path
from . import views

app_name = 'shop'  # důležité pro jmenný prostor URL

urlpatterns = [
    path('', views.home, name='home'),  # domovská stránka
    path('kategorie/', views.categories, name='categories'),  # seznam kategorií
    path('kategorie/<int:pk>/', views.category_detail, name='category_detail'),  # detail kategorie s produkty
    path('produkty/', views.products, name='products'),  # seznam produktů (možno s vyhledáváním)
    path('produkt/<int:pk>/', views.product_detail, name='product_detail'),  # detail produktu
    path('kontakt/', views.contact, name='contact'),  # kontaktní stránka
]
