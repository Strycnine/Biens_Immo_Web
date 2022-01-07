# Biens Immo Web


## Prérequis :

 - [Python 3.x](https://www.python.org/downloads/)
 - [Requirements.txt](./requirements.txt)

---

## Utilisation :

  1. Récupérez le [repository](https://github.com/Strycnine/Biens_Immo_Web/archive/refs/heads/main.zip).
  1. installez le [Requirements.txt](./requirements.txt).
  1. Allez dans le fichier `Biens_Immo_Web\Biens_Immo_Web\setting.py`
  1. Modifier selon vos besoin les entrées suivante :
  ```python
  EMAIL_HOST = 'smtp.gmail.com' # A modifier suivant votre boite mail
  EMAIL_HOST_USER = 'votre mail'
  EMAIL_HOST_PASSWORD = 'votre mot de passe'
  ```
  1. Ouvrez un shell a partir du dossier `Biens_Immo_Web`.
  1. Lancez la commande `python manage.py runserver`.
  1. Ouvrez votre navigateur -> http://127.0.0.1:8000
  1. It's GOOD ! :upside_down_face:

---

## Interface :

Les identifiants pour notre exemple :
```
Username : Admin
Password : 123
```

### Page d'accueil : 

La première page que vous allez voir, celle qui regroupe la vue global des données.
A partir de cette page on peut également envoyer un mail récapitulatif des données présentes.

<img src="https://user-images.githubusercontent.com/86345325/148593221-742186a5-7a0b-42f9-a41e-522db6a6e213.png" alt="Page_Data_View" width="75%">

### Page de login : 

La page d'authentification qui permet d'accéder à l'upload de nouvelles données.

<img src="https://user-images.githubusercontent.com/86345325/148592125-b908bf18-fe24-4e5e-bc6f-86f1d62294f8.png" alt="Page_Login" width="75%">

### Page d'upload : 

Ici les personnes autorisés peuvent uploader un nouveau fichier `.CSV`.

<img src="https://user-images.githubusercontent.com/86345325/148593229-5b021240-1cc3-4ffc-8855-3ab7f9c07bc1.png" alt="Page_Upload_CSV" width="75%">

### Page admin : 

C'est à partir de là que l'on peut gérer les accès, modifier les données et choisir l'adresse mail à laquelle le récapitulatif est envoyer.

<img src="https://user-images.githubusercontent.com/86345325/148593207-34720811-bfaa-4db6-b428-edd93c22d5a0.png" alt="Page_Admin" width="75%">
