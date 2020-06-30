from django.urls import path,include
from . import views

urlpatterns = [
   	path('', views.index),
    path('trial',views.trial,name='trial'),
    path("add",views.get,name="tri"),

  # path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
]
