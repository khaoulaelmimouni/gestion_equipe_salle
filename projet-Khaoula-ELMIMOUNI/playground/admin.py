from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Equipe
from .models import salle
 
admin.site.register(Equipe)
admin.site.register(salle)
