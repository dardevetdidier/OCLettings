## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Le déploiement utilise un pipeline CircleCi:
* Tests / Linting
* Dockerisation du projet (création de l'image docker du projet)
* Déploiement sur Heroku

### Prérequis
- compte [Docker](https://www.docker.com/)
- compte [Heroku](https://www.heroku.com/)
- compte [circleci](https://circleci.com/)
- compte [Sentry](https://sentry.io/welcome/)

### Configurer Sentry
- Connectez vous à votre compte Sentry
- Créer un nouveau projet
- Les fichiers du projet sont déjà configurés

### Configurer Heroku
- Créer l'application heroku 'oc-lettings-v01'
- Dans les paramètres de l'application, cliquer sur le bouton 'Reveal Config Vars' pour ajouter une varialble d'environnement
  * DJANGO_SECRET_KEY=votrecléDjango
  * SENTRY_DSN=VotreSentryClientDSN (cliquer sur 'client keys' dans les paramètres de l'application dans Sentry)

### Configurer Circleci
- Se connecter avec son compte Github et configurer le projet OCLettings
- spécifier l'utilisation du fichier config.yml existant
- Dans les paramètres de l'application définir 2 variables d'environnement:
  * HEROKU_APP_NAME=oc-lettings-v01
  * HEROKU_API_KEY=VotreCléAPIHeroku (Voir dans les paramètres de vorte compte Heroku)
  * DJANGO_SECRET_KEY=VotreCléSecrèteDjango
  * DOCKER_PASS=VotreMotdePasseDocker
  * DOCKER_USER=VotreNomUtilisateurDocker
  * SENTRY_DSN=VotreSentryClientDSN

### Exécuter le déploiement via CircleCi

Pour lancer le pipeline du déploiement via circleci, il vous suffit de faire un commit et un push
sur Github.  

### Accéder à l'application

Se rendre à l'adresse https://oc-lettings-v01.herokuapp.com

### Accéder au log Sentry

Se rendre à l'adresse https://oc-lettings-v01.herokuapp.com/sentry-debug/


## Lancer l'application via docker image

Une fois le pipeline circleci effectué une image docker est crée sur circleci-hub.
Pour lancer l'application il faut récupérer cette image et l'exécuter.

### Récupérer l'image
* Dans votre compte docker noter la dernière version de l'image (oclettings:0.1.[n])
* Dans un terminal\
```$ docker pull [votrenomutilisateurCircleCi]/oclettings:1.1.[n]```

### Lister les images
Lister les images permet de récupérer l'id de l'image à exécuter\
```$ docker images```

### Exécuter l'image
```docker run -it -e DJANGO_SECRET_KEY=[cléDjango] -p 8000:8000 [image_id]```

