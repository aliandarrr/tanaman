from django.urls import path
#from todolist import views
from . import views

urlpatterns = [
    path('login/', views.login),
    path('Home/', views.Home),
    path('galeri/', views.galeri),
    path('About/', views.About),
    path('Contact/', views.Contact),
    path('Tanaman_Hias/', views.Tanaman_Hias),
    path('TanamanBuah/', views.TanamanBuah),
    path('TanamanSayur/', views.TanamanSayur),
    path('lainlain/', views.lainlain),
    path('edit/<int:id>', views.edit),
    path('hapus/<int:id>', views.hapus)
]