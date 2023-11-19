from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_list, name='data_list'),
    path('equipe/<str:id_equipe>/', views.detail_equipe, name='detail_equipe'),
    path('sallee/<str:id_salle>/', views.detail_salle, name='detail_salle'),
    path('create_equipe/', views.create_equipe, name='create_equipe'),
    path('create_salle/', views.create_salle, name='create_salle'),
    path('delete_salle/<str:id_salle>/', views.delete_salle, name='delete_salle'),
    path('delete_equipe/<str:id_equipe>/', views.delete_equipe, name='delete_equipe'),
    path('modify_equipe/<str:id_equipe>/', views.modify_equipe, name='modify_equipe'),
    path('modify_salle/<str:id_salle>/', views.modify_salle, name='modify_salle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)