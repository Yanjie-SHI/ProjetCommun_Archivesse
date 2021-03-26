# ProjetCommun_Archivesse

Sujet : Il était une fois...
Membre : Yanjie SHI
Encadré par : M.Cyril LACHEZE et Mme. Floriane OWXZAREK

Cible : Historiens qui ne peuvent pas aller au centre d'archives éloigné
IDE : Pycharm
BDD : Navicat

Base de Dasonnées : 
1 - Changer le mot de passe local pour Mysql dans le fichier settings.py à ligne 84
2 - Pour étalir la BDD, tapez la command : python3 manage.py makemigrations 
                                           python3 manage.py migrate
                                           python3 manage.py makemigrations app01
                                           python3 manage.py migrate app01
                                           python3 manage.py loaddata app01.json

Pycharm : 
1 - Installer les plugins
2 - Edit configuration : Add new configuration -> Python -> Script path (la path de fichier manage.py) -> Paramètres(runserver 0.0.0.0:8000) -> Apply -> OK
3 - Démarrer avec Débug

Navigator :
1 - Taper : localhost:8000

Crontab :
1 - Installer Crontab dans Pycharm
2 - Changer le path avec _________________(path local de projet)/ProjetCommun_Archivesse/app01/scheduler.log dans le settings.py à ligne 161
2 - Pour activer la mission crontab, tapez la command : python manage.py crontab add　　  
3 - Pour arrêter la mission crontab, tapez la command : python manage.py crontab remove 
4 - Pour montrer le status de la mission crontab, tapez la command : python manage.py crontab show 
