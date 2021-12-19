from django.shortcuts import render, redirect
from Upload_CSV.models import Immo
from Upload_CSV import models
import pandas as pd
import json


def data_view(request):
    if request.method == 'POST' and 'file' in request.FILES:
        data = pd.read_csv(request.FILES["file"])
        json_records = data.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)
        immo = models.Immo()
        for i in data:
            immo.id = i['index']
            immo.id_lot = i['id_lot']
            immo.nb_piece = i['nb_piece']
            immo.typologie = i['typologie']
            immo.prix_tva_reduite = i['prix_tva_reduite']
            immo.prix_tva_normale = i['prix_tva_normale']
            immo.prix_HT = i['prix_HT']
            immo.prix_m2_HT = i['prix_m2_HT']
            immo.prix_m2_TTC = i['prix_m2_TTC']
            immo.surface = i['surface']
            immo.etage = i['etage']
            immo.orientation = i['orientation']
            immo.exterieur = i['exterieur']
            immo.balcony = i['balcony']
            immo.garden = i['garden']
            immo.parking = i['parking']
            immo.nom_programme = i['nom_programme']
            immo.ville = i['ville']
            immo.departement = i['departement']
            immo.date_fin_prog = i['date_fin_programme']
            immo.adresse = i['adresse_entiere']
            immo.promoteur = i['promoteur']
            immo.date_extraction = i['date_extraction']
            immo.save()
        return redirect('/')
    else:
        title = 'Visualisation de la Data'
        data = pd.DataFrame(list(Immo.objects.all().values()))
        nb_biens = data[data['balcony']=='False'].shape[0]
        ecart = round(data['prix_tva_normale'].std(axis=0), 2)
        moy_ville = round(data[['ville','prix_tva_normale']].groupby(['ville'], as_index=False).mean(),2)
        json_records = moy_ville.reset_index().to_json(orient='records')
        moy_ville = []
        moy_ville = json.loads(json_records)
        context = {
            "title" : title,
            "nb_biens" : nb_biens,
            "ecart" : ecart,
            "moy_ville" : moy_ville,
        }
        return render(request, 'result.html', context)
