
from django.urls import path,include
from . import views
urlpatterns = [
    path('product/',views.product),
    path('',views.products),
]
