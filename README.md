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

## Déploiement :
FAIT AVEC:<br>
https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR/tree/1b45bda8dcdeac129d2c88b7511191c8d066c7b7 <br>
(Python-OC-Lettings-FR commit du 17/09/2020) <br>
L'application est automatiquement déployée à chaque commits qui sont push dans le repository Git. Pour les branches autres que master, la pipeline exécutera toutes les étapes jusqu'au test. Pour la branche master, la Pipeline exécutera toutes les étapes, dont également la conteneurisation ainsi que le déploiement sur Internet.

La pipeline CI/CD installe toutes les dépendances elle-même.
Elle envoie l’app sur Heroku sous le nom de `p13-open-classrooms`. 
Si aucune application sous ce nom existe, le déploiement ne fonctionnera pas.

Si vous voulez déployer le site après avoir changé le code, vous n’avez rien à faire.
CircleCI détectera tout changement sur le repo GitHub et déclenchera une pipeline automatiquement, qui viendra déployer ou redéployer l’app sur Heroku toute seule.

Si vous voulez re-déployer le site sans avoir changé le code, vous pouvez utiliser le bouton “Rerun workflow from start” dans la colonne “actions” de la liste des pipelines dans CircleCI.
Attention, choisissez la bonne pipeline.

Si vous voulez rendre l’application déployée inaccessible, vous pouvez activer le Maintenance Mode dans les settings de votre application Heroku.

Les builds CI/CD sont visible içi:<br>
https://app.circleci.com/pipelines/github/Ekmah/P13

Attention, de multiples variables d'environnement sont utilisées.<br>
Les variables DOCKER_USERNAME, DOCKER_LOGIN, HEROKU_API_KEY ainsi que HEROKU_APP_NAME sont défini dans les paramètres du projet CircleCI.<br>
Les variables d'environnement HEROKU_API_KEY et HEROKU_APP_NAME sont automatiquement utilisées par `heroku container:login` dans le config.yml<br>
Les variables SECRET_KEY et SENTRY_DSN sont définies dans un fichier .env dans le même dossier que le fichier settings.py.

