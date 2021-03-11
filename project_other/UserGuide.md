## business logic  
- search archive
    - anyone who want to know info of a certain archive, or keyword of archives
- search reservation
- search demand  
    - this is for person who has certain digital archive backup on his disk, he search for demands who need this archive
    - for people who need an digital archive regardless of whether there is a suitable reservation, he can create a demand directly from the link in search page
    

## Done
- welcome: Commence votre visite
- header: Me connecter -> login / Espace Personnel -> self_center
- login: login logic, interaction with database, jump to search page
- search: 
    - Toutes les archives / Archives numérisées / Producteurs d'archives: switch background change
    - Tous les mots saisis: click to show/hide search particle view
    - Recherch / Rendez-vous indicator show/hide when cliced
- archive detail
- reservation detail
- self_center:
    - profile / favorites / message_list / reservation / logout click to jump to relevant page
    - logout logic (clear browser session and cache, return to search page)
- message detail
       
## TODO list
- archive detail page return button (jump to search result list)
- reservation detail page return button
- favorites table create



## URLs
```djangourlpath
url('admin/', admin.site.urls),
url(r'^$', views.welcome),
url(r'^search', views.search),
url(r'^archivedetail', views.archive_detail),
url(r'^login', views.login),
url(r'^register', views.register),
url(r'^selfcenter', views.self_center),
url(r'^messagelist', views.message_list),
url(r'^profile', views.profile),
url(r'^favorites', views.favorites),
url(r'^addfavorites', views.add_favorites),
url(r'^reservation', views.reservation),
url(r'^logout', views.logout),
```

## MySQL settings
- Create database manually in Navicat (database name: web_historien)
- Config MySql connections in web_historien/settings.py  
```python
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'web_historien',  
        'USER': 'root',  
        'PASSWORD': 'root',  
        # Set to empty string for localhost.  
        'HOST': '',  
        # Set to empty string for default.  
        'PORT': '',  
    }  
}
```
- Edit tables in app01/models.py  
<font color=red>**\* Note: Don't use French in db, MySQL will ommit French characters like èéùçà etc.**</font>
- Run the following 2 commands in iTerm or PyCharm Terminal  
<font color=red>**\* Note: This is to auto create tables in MySql db.**</font>
```shell script
$ python3 manage.py makemigrations  
$ python3 manage.py migrate  
$ python3 manage.py loaddata app01.json
```
- Migrate command will also create tables that django needed, like auth_user, django_session etc.  
<font color=red>**\* Remember not to delete these tables.**</font>
  

## Note other  
- If you create tables from MySQL client(navicat), and want to generate models.py file automatically, use the following command:   
```shell script
$ python3 manage.py inspectdb Users Archive Museum Reservation Res_Dem_Arch > app01/models.py
```

- dump data from db to fixture
```shell script
$ python3 manage.py dumpdata app01 --format=json --indent=4 > app01/fixtures/app01.json
```

- Providing initial data for models  
    - Providing data with fixtures, create a *.fixture file under project/app01/fixture directory, this needs to be added for each app in a project
    - use the following commad to load data into db  
```
[
  {
    "model": "myapp.person",
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  },
  {
    "model": "myapp.person",
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  }
]
```

```shell script
$ python3 manage.py loaddata <fixturename> 
```

- Django admin page: http://localhost:8000/admin, there is a username and password, we need to generate a super user by following command:  
```shell script
$ python3 manage.py createsuperuser
```

- export Class Diagram from project
    1. install graphviz on Mac  
    2. install pylint and graphvi in django(python) project  
    3. run command from virtualenv  
```shell script
brew install graphvi  # for mac
apt-get install graphviz  # for ubuntu
# for windows, install from their website: http://www.graphviz.org/download/ 
```
    
```
pip install pylint
pip install graphviz
```
    
```
pyreverse ./app01 -o mydiagram.png 
```
  
    
    