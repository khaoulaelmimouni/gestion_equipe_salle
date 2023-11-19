from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class salle(models.Model):
    id_salle = models.CharField(max_length=100, primary_key=True)
    capacite = models.IntegerField()
    occupe = models.BooleanField(default=False)
    image = models.ImageField(upload_to='salles/', blank=True, null=True)

    def __str__(self):
        return self.id_salle

class Equipe(models.Model):
    id_equipe = models.CharField(max_length=100, primary_key=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    situation = models.CharField(max_length=20, choices=[('interieur', 'Intérieur'), ('exterieur', 'Extérieur')])
    adversaire = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    lieu = models.ForeignKey(salle, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_equipe

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['adversaire'], name='unique_adversaire_per_equipe')
        ]

    def save(self, *args, **kwargs):
        
        self.lieu.occupe = (self.situation == 'interieur')
        self.lieu.save()
        super().save(*args, **kwargs)





        
# models.ImageField(upload_to='stades/', blank=True, null=True)
#models.CharField(max_length=200)