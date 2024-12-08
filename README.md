# Mini-Application-E-Commerce
une petite application qui permet de gérer les produits d’un catalogue et d’afficher leur disponibilité en stock ||Backend (Django) || Frontend (Vue.js) .

# Configuration de l'environnement :
1. Prérequis
Avant de commencer, assurez-vous d'avoir installé les outils suivants sur votre machine :
* Python (pour le backend avec Django)
* Node.js (pour le frontend avec Vue.js)
* pip (pour installer les packages Python)
* npm (pour installer les packages Node.js)
# 2. Configuration du backend
a. Cloner le repository
Dans votre terminal, clonez le repository du projet :

[git clone https://github.com/brahmiiheb/Mini-Application-E-Commerce.git]
+ cd Mini-Application-E-Commerce
b. Créer un environnement virtuel
Créez un environnement virtuel pour isoler les dépendances :
python -m venv venv
c. Activer l'environnement virtuel
Sur Windows : Avant d'activer l'environnement virtuel, vous devrez peut-être exécuter cette commande pour permettre les scripts PowerShell :

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Ensuite, activez l'environnement virtuel avec la commande suivante :

.\env\Scripts\Activate

Sur macOS/Linux :

source env/bin/activate

Ensuite, installez les dépendances via pip :

pip install -r requirements.txt

d. Configurer les variables d'environnement
e. Lancer le backend
Pour démarrer le serveur de développement Django, utilisez la commande suivante :

python manage.py runserver
Cela lancera le backend sur http://127.0.0.1:8000/.

# 3. Configuration du frontend
a. Se rendre dans le répertoire frontend
Naviguez dans le dossier du frontend  :

cd frontend

b. Installer les dépendances Node.js
Installez les dépendances nécessaires avec npm :

npm install

c. Lancer le frontend
Pour démarrer le serveur de développement Vue.js, utilisez la commande suivante :

npm run serve
Cela lancera le frontend sur http://localhost:8080/.

# Tests
Pour exécuter les tests unitaires du backend, utilisez la commande suivante :

python manage.py test apps.products

Conclusion
Une fois ces étapes complétées, le backend sera accessible via http://127.0.0.1:8000/ et le frontend via http://localhost:8080/. Vous pouvez maintenant tester les interactions entre les deux parties.
