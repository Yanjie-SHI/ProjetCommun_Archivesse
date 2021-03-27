# Internationalization – Settings
Let’s work on how we can implement internationalization, i.e. that our page can support multiple languages.

* First, we will create a folder to save all the translation files. Those files will be created automatically by Django, writing the strings that we want to translate. I’ll show you how you can tell Django which strings you want to translate latter, but the idea is that you edit the files and put the translation for each string manually. This way, Django will choose one language or another depending on the user preferences.

* The translation’s folder will be located inside the taskbuster folder:
```
$ mkdir web_historien/locale
```

* Next, open your settings.py file and make sure you have
```
USE_I18N = True
```
and the template context processor django.template.context_processors.i18n is inside the TEMPLATES['OPTIONS']['context_processors'] setting:
```
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.i18n',
            ],
        },
    },
]
```

Note: You can also find the value of a specific setting by using the Django shell. For example:
```
$ python manage.py shell
>>> from django.conf import settings
>>> settings.TEMPLATES
```
and it will output the current value of that variable.

* Next, add the Locale middleware in the correct position, to be able to determine the user’s language preferences through the request context:
```
MIDDLEWARE_CLASSES = (
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
)
```

* Next, specify the languages you want to use:
```
from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)
```
We will use English and French (but feel free to put the languages you want, you can find its codes here). The ugettext_lazy function is used to mark the language names for translation, and it’s usual to use the function’s shortcut _.

Note: there is another function, ugettext, used for translation. The difference between these two functions is that ugettext translates the string immediately whereas ugettext_lazy translates the string when rendering a template.

For our settings.py, we need to use ugettext_lazy because the other function would cause import loops. In general, you should use ugettext_lazy in your model.py and forms.py files as well.

Moreover, the LANGUAGE_CODE setting defines the default language that Django will use if no translation is found. I’ll leave the default:
```
LANGUAGE_CODE = 'en-us'
```

* And finally, specify the locale folder that we created before:
```
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
```
Don’t forget the trailing coma.


# Internationalization – Urls
Ok, now that we have configured the settings, we need to think about how we want the app to behave with different languages. Here we will take the following approach: we will include a language prefix on each url that will tell Django which language to use. For the Home page it will be something like:
```
mysite.com/en
mysite.com/ca
```
And for the rest of urls, like mysite.com/myapp, it will be:
```
mysite.com/en/myapp
mysite.com/ca/myapp
```
This way the user may change from one language to another easily. 

However, we don’t want that neither the robots.txt nor the humans.txt files follow this structure (search engines will look at mysite.com/robots.txt and mysite.com/humans.txt to find them).
One way to implement this is with the following urls.py file:
```python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
]

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
```
Note that we left the robots.txt and humans.txt files with the same url, and the ones that we want to be translated use the i18n_patterns function.

Run your local server and visit the home page, it should redirect to /en or /ca. You can learn more about how Django discovers language preference in the official documentation.

But how does the user change its language preferences? Well, Django comes with a view that does this for you 😉

This view expects a POST request with a language parameter. However, we will take care of that view in another time in this tutorial, when customizing the top navigation bar. The idea is to have a drop-down menu with all the possible languages, and just select one to change it.

Before proceeding, let’s run our tests,
```
$ python mange.py test taskbuster.test
```
Oh…. one failed! Well actually both unittest in taskbuster/test.py fail, as the template rendered when trying to use reverse("home") is not found. This is because we need to set an active language for the reverse to work properly. First, write this at the top of the file:
```
from django.utils.translation import activate
```
and next, activate the selected language just after the test declaration. For example:
```
def test_uses_index_template(self):
    activate('en')
    response = self.client.get(reverse("home"))
    self.assertTemplateUsed(response, "taskbuster/index.html")
```
And the same for the other test: test_uses_base_template.

Now, tests pass. You should do the same for the functional_tests/test_all_users.py: import the activate method at the beginning of the file and add the activate(‘en’) as the last step on the setUp method.

# Internationalization – Templates
Let’s focus now on how we can translate the h1 Hello World title of the Home Page. Open the index.html template and look for <h1>Hello, world!</h1>.

We will use two different template tags:

trans is used to translate a single line – we will use it for the title
blocktrans is used for extended content – we will use it for a paragraph
Change the h1 and p contents of the jumbotron container for the following code:
```djangotemplate
<div class="jumbotron">
    <div class="container">
        <h1>{% trans "Welcome to TaskBuster!"%}</h1>
        <p>{% blocktrans %}TaskBuster is a simple Task manager that helps you organize your daylife. </br> You can create todo lists, periodic tasks and more! </br></br> If you want to learn how it was created, or create it yourself!, check www.django-tutorial.com{% endblocktrans %}</p>
        <p><a class="btn btn-primary btn-lg" role="button">Learn more &raquo;</a></p>
      </div>
    </div>
</div>
```
Moreover, to have access to the previous template tags, you will have to write {% load i18n %} near the top of your template. In this case, after the extends from base.html tag.

Internationalization – Translation
Finally, we are able to translate our strings!

Go to the terminal, inside the taskbuster_project folder (at the same level as the manage.py file), and run:

$ python manage.py makemessages -l ca
1
$ python manage.py makemessages -l ca
This will create a message file for the language we want to translate. As we will write all our code in english, there is no need to create a message file for that language.

But ohh!! we get an ugly error that says that we don’t have the GNU gettext installed (if you don’t get the error, good for you! skip this installation part then!). Go to the GNU gettext home page and download the last version. Inside the zip file you’ll find the installation instructions on a file named INSTALL.

Basically, you should go inside the package folder (once unzipped) and type:

$ ./configure
1
$ ./configure
to configure the installation for your system. Next, type

$ make
1
$ make
to compile the package. I always wonder why some installations print all that awful code on your terminal!

If you want, use

$ make check
1
$ make check
to run package tests before installing them, to see that everything works. Finally, run

$ make install
1
$ make install
to install the package.

Okey! Let’s go back to our developing environment, and try to generate our message file!

$ python manage.py makemessages -l ca
1
$ python manage.py makemessages -l ca
Yes! It worked!

Now go to the taskbuster/locale folder to see what’s in there.

$ cd taskbuster/locale
$ ls
1
2
$ cd taskbuster/locale
$ ls
There is a folder named ca (or the language you chose to translate) with a folder named LC_MESSAGES inside. If you go inside it, you’ll find another file named django.po. Inspect that file with your editor.

There is some metadata at the beginning of the file, but after that you’ll see the strings we marked for translation:

The language’s names “English” and “Catalan” in the base.py settings file
The Welcome to TaskBuster! title on the index.html file
The paragraph after the title on the index.html file
Each of these sentences appear in a line beginning with msgid. You have to put your translation in the next line, the one that starts with msgstr.
Translating the title is simple:

msgid "Welcome to TaskBuster!"
msgstr "Benvingut a TaskBuster!"
1
2
msgid "Welcome to TaskBuster!"
msgstr "Benvingut a TaskBuster!"
And with a paragraph, you have to be careful to start and end each line with "":

msgid ""
"TaskBuster is a simple Task manager that helps you organize your daylife. </"
"br> You can create todo lists, periodic tasks and more! </br></br> If you "
"want to learn how it was created, or create it yourself!, check www.django-"
"tutorial.com"
msgstr ""
"TaskBuster és un administrador senzill de tasques que t'ajuda a administrar "
"el teu dia a dia. </br> Pots crear llistes de coses pendents, tasques "
"periòdiques i molt més! </br></br> Si vols apendre com s'ha creat, o"
"crear-lo tu mateix!, visita la pàgina <a href='http://www.marinamele.com/taskbuster-django-tutorial' target=_'blank'>Taskbuster Django Tutorial</a>."
1
2
3
4
5
6
7
8
9
10
msgid ""
"TaskBuster is a simple Task manager that helps you organize your daylife. </"
"br> You can create todo lists, periodic tasks and more! </br></br> If you "
"want to learn how it was created, or create it yourself!, check www.django-"
"tutorial.com"
msgstr ""
"TaskBuster és un administrador senzill de tasques que t'ajuda a administrar "
"el teu dia a dia. </br> Pots crear llistes de coses pendents, tasques "
"periòdiques i molt més! </br></br> Si vols apendre com s'ha creat, o"
"crear-lo tu mateix!, visita la pàgina <a href='http://www.marinamele.com/taskbuster-django-tutorial' target=_'blank'>Taskbuster Django Tutorial</a>."
Also, note the final space at the end of the line. If you don’t include that space, the words at the end of the line and at the beginning of the next line will concatenate.

Once you have all the translations set, you must compile them with:

$ python manage.py compilemessages -l ca
1
$ python manage.py compilemessages -l ca
You can run your local server and see the effect by going to the home page, but I prefer writing a test first! 🙂

In the functional_tests/test_all_users.py add the following tests:

def test_internationalization(self):
    for lang, h1_text in [('en', 'Welcome to TaskBuster!'),
                                ('ca', 'Benvingut a TaskBuster!')]:
        activate(lang)
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.text, h1_text)
1
2
3
4
5
6
7
def test_internationalization(self):
    for lang, h1_text in [('en', 'Welcome to TaskBuster!'),
                                ('ca', 'Benvingut a TaskBuster!')]:
        activate(lang)
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.text, h1_text)
Remember to change the Benvingut a TaskBuster!  sentence and the activate('ca') if you’re using another language!

I hope all of your tests passed! 🙂