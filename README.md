# UA-M2-EC903-Django-Honey-Pot

## Déploiment

### AlwaysData

Le site sera déploiyé sur les serveurs de AlwaysData.

#### Créer un compte sur AlwaysData

https://www.alwaysdata.com/fr/

#### Dans la rubrique Web -> Site

- Rentrez dans les paramètres du serveur en cliquant sur l'engrenage

- Dans Configuration -> Type Choisir Python WSGI
- Dans Configuration -> Chemin  mettez le chemin suivant
`` /www/ua-m2-ec903-django-honey-pot/project/project/wsgi.py
``
- Dans Configuration -> Répertoir de travail mettez le chemin suivant ``/www/ua-m2-ec903-django-honey-pot/project/``

- Dans Configuration -> Version de Python selectionnez *3.6.6*

- Dans Configuration -> Répertoir du virtualenv mettez le chemin suivant ``/venv/``

- Dans Configuration -> Chemins statiques mettez le chemin suivant ``/static/=/www/ua-m2-ec903-django-honey-pot/project/static/``

#### Dans la rubrique Environement -> Python
-  selectionner *Python 3.6.6*

#### Accès distant -> SSH

- Modifier l'utilisateur SSH déjà créé
- Mettre un mot de passe et activer la connexion par mot de passe

### Configuration

#### Environnement Virtuel
- A la racine créer l'environement virtuel
```
python -m venv venv
```

- Activer l'environement virtuel
```
source venv/bin/activate
```
- Installez Django (obligatoirement avec le venv activé)
```
pip install Django
```



#### Récupération
- Dans le dossier www/ faites un git clone du projet

```
git clone https://github.com/lebenef/ua-m2-ec903-django-honey-pot.git
```

#### Django

- Se rendre dans le dossier contenant le *manage.py*
```
cd www/ua-m2-ec903-django-honey-pot/project/
```

- Effectuer la migration de l'application
```
python manage.py migrate
```

- Créer le super utilisateur de la base de données
```
python manage.py createsuperuser
```

### Lancement

- Retrouner dans la rubrique Web -> Site et redémarrer le serveur

- Rendez-vous sur le lien du site.

- Vous pouvez voir les données saisies en base en allant sur : ``http://nom-du-compte.alwaysdata.net/admin`` et utiliser les iditifiant que vous avez saisies
