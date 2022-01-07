from django.db import models


# Create your models here.
class Immo(models.Model):
    id = models.IntegerField(primary_key=True)
    id_lot = models.CharField(max_length=120,null=True)
    nb_piece = models.IntegerField()
    typologie = models.CharField(max_length=20)
    prix_tva_reduite = models.FloatField(null=True)
    prix_tva_normale = models.FloatField(null=True)
    prix_HT = models.FloatField(null=True)
    prix_m2_HT = models.FloatField(null=True)
    prix_m2_TTC = models.FloatField(null=True)
    surface = models.FloatField()
    etage = models.IntegerField(null=True)
    orientation = models.CharField(max_length=50)
    exterieur = models.CharField(max_length=10)
    balcony = models.CharField(max_length=10)
    garden = models.CharField(max_length=10)
    parking = models.CharField(max_length=10)
    nom_programme = models.CharField(max_length=50)
    ville = models.CharField(max_length=80)
    departement = models.IntegerField()
    date_fin_prog = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)
    promoteur = models.CharField(max_length=50)
    date_extraction = models.CharField(max_length=20)


class Contact(models.Model):
    sujet = models.CharField(max_length=64,null=True)
    message = models.CharField(max_length=256,null=True)
    destinataire = models.CharField(max_length=32,null=True)
