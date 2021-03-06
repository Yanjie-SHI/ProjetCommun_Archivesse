## business logic  
- search archive
    - anyone who want to know info of a certain archive, or keyword of archives
- search reservation
- search demand  
    - this is for person who has certain digital archive backup on his disk, he search for demands who need this archive
    - for people who need an digital archive regardless of whether there is a suitable reservation, he can create a demand directly from the link in search page

       
## TODO list
- 2021/04/08
    - 登录后跳转回前一个页面
    - 注册js校验，密码和重复密码是否一致，是否为8位密码
    - after switch language, should go back to previous page user viewed
    - css fix: search result resv filter tags floating  √
    - css fix: create/join resv: user info email tag too short, shouldn't change line  √
    - bug fix: after terminate demand in personal space, page didn't refresh  √
    - bug fix: switch language after login, cannot show login user name  √
    - back link, refresh request result  √
- 2021/04/07
    - bug fix: resv create switch museum, some archive code/folio would not be shown  √
    - my message page: message type selector  √
    - add all messages: create resv, join resv, unjoin resv, finalize resv(cron job), create demand, delete demand, terminate demand, register, update profile  √ 
    - paginator for personal space list page  √ except all prev & next button
    - filter tag x button in search result resv page  √
- 2021/04/06
    - js timer task, fetch data from server Notification table, if there are data, show an icon on header  √
    - after read the message, put the status to 'already read'  √
    - personal space my favorite page fetch data from server  √
    - globalization for all pages √ except in js & return from server
- 2021/04/04
    - search filter in search result resv page  √ .. exclude all filter tag X button
    - globalization  √ half (welcom, login,header,main,search result archive, search result resv,)
- 2021/03/28
    - search resv: type in 3 characters in museum input, popup a list containing all relavant museums  √
    - search archive func in search result archive page  √
    - search resv func in search result resv page  √
    - search demand func in search result demand page  √
    - bugfix: empty post code cause register failed with error  √
    - cssfix: resv creator view: css error for one joiner with multiple archives  √
    - resv creator view: when change go or not checkbox, after success alert, should not jump back to last page, but stay at current page  √
    - resv creator view: when click on send link, after success alert, refresh current page  √
- 2021/03/23
    - multilanguage select frame  √
    - message detail page  √
    - selfcenter each sub page return link  √
    - profile page error  √
    - finished resv should not show in 'En cour' tab  √
    - my message page fetch data from db  √
    - resv and demand search page, add create button directly  √
    - 预约成功的站内信  √
    - header的书图标，回到文献搜索页面  √
    - 预约查询结果页面，2个新建按钮一高一低  √
    - 预约去过的状态，不要再搜索结果里展示  √
    - 标题栏添加退出按钮  √
    - msgbox confirm按钮，文字改成Confirmer  √
    - 搜索预约，不加任何参数空搜，报错  √
    - 创建预约的博物馆名称和日期要从搜索结果页带过来  √
    - 创建预约第一个地址为空  √
    - search demand result, help button need login verify  √
    - My reservation 已完成列表  √
- 2021/03/19
    - 需求部分：创建需求，我的需求页，需求搜索结果页  √
    - 注册功能 √
- 2021/03/14
    - 创建和加入的成功提示框，确定后返回上一个页面  √  但上一个搜索结果页还得刷新
    - 预约加入时创建Res_Dem_Confirm_Status  √
    - 加一个定时任务，时刻监测对于所有reservation，是否所有demander都确认了收获，是就把reservation status设成2已结束  √
    - 预约creatorview 根据Res_Dem_Confirm_Status表数据获取是已发送按钮还是待发送按钮，非reservation.status  √
    - 预约creatorview Envoye按钮点击时更新Res_Dem_Confirm_Status记录  √
    - selfcenter 预约demander confirm按钮，在原始已发送的数据上更新状态received=1  √
    - 预约creatorview Oui和Non 点击时更新Reservation表的状态为1  √
    - 把提示框垂直居中  √
    - 创建预约默认数字为0，让用户自己选成其他的  √
    - 创建预约的蓝色按钮文字改成Confirmer  √
    - 创建预约页面 Annuler 取消返回上一页  √
    - 加入预约，默认可用数也改成0  √
    - 加入预约，选成2以后，创建了10以后的所有input 框  √
    - 预约creatorview email前面的提示文字  √
- 2021/03/12
    - archive detail page return button (jump to search result list)
    - reservation detail page return button
    - favorites table create



## URLs
```djangourlpath
url('admin/', admin.site.urls),
url(r'^$', views.welcome),
url(r'^to_search', views.to_search),
url(r'^search_archive', views.search_archive),
url(r'^search_resv', views.search_resv),
url(r'^search_demand', views.search_demand),
url(r'^archive_detail', views.archive_detail),
url(r'^login', views.login),
url(r'^register', views.register),
url(r'^selfcenter', views.self_center),
url(r'^messagelist', views.message_list),
url(r'^message_detail', views.message_detail),
url(r'^profile', views.profile),
url(r'^favorites', views.favorites),
url(r'^add_favorites', views.add_favorites),
url(r'^remove_favorites', views.remove_favorites),
url(r'^logout', views.logout),

url(r'^to_my_reservation', views_resv.to_my_reservation_list),
url(r'^to_resv_detail_creatorview', views_resv.to_resv_detail_creatorview),
url(r'^to_create_resv', views_resv.to_create_reservation),
url(r'^create_resv', views_resv.create_reservation),
url(r'^join_resv', views_resv.join_reservation),
url(r'^undo_join_resv', views_resv.undo_join_reservation),
url(r'^confirm_sent_receive_status', views_resv.confirm_sent_receive_status),
url(r'^update_resv_status', views_resv.update_resv_status),

url(r'^to_my_demand', views_demand.to_my_demand),
url(r'^to_create_demand', views_demand.to_create_demand),
url(r'^create_demand', views_demand.create_demand),
url(r'^terminate_demand', views_demand.terminate_demand),
url(r'^delete_demand', views_demand.delete_demand),

url(r'^fetchmuseumaddress', utils.fetch_museum_address),
url(r'^fetchmuseumname', utils.fetch_museum_name),
url(r'^verify_login', utils.verify_login_js),
url(r'change_language', utils.change_language),
url(r'fetch_my_mew_message_for_header_icon', views.fetch_my_mew_message_for_header_icon),
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
  
## Develop Tips
- use prop to set radio/checkbox checked in js
```javascript
$("#archiveTypeRadios1").prop("checked", "checked");
$("#archiveTypeRadios1").removeAttr("checked");
```    
- set a scheduler task in js
```javascript
var myInterval = setInterval(function () {
    console.log('it works' + new Date());
},30000);  // milliseconds
clearInterval(myInterval);
```
- return to the previous page and reload page in js
```javascript
window.location=document.referrer;
```