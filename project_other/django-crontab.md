jianshu.com/p/27f003149090

## django使用django-crontab实现定时任务

在做一个django项目的时候，我遇到了一个定时任务的需求，我这里是需要定时扫描数据库并发送邮件，在查阅相关资料后，总结出如下几个方法

- 使用while创建一个死循环，判断时间，从而执行一些函数
- 使用APScheduler库实现定时任务 （详情可以见http://blog.csdn.net/hui3909/article/details/46652623）
- django-crontab实现定时任务
- django-celery实现定时任务  

在我斟酌再三，最终还是选择了django-crontab这个方法，这个方法最契合我的需求，同时也相对简单，所以本文也就着重介绍一下

## django-crontab安装
* 安装django-crontab库  
这里使用pip安装即可，在终端输入以下命令即可  
pip install django-crontab

* 在工程里使用django-crontab  
在django项目的settings.py的INSTALLED_APPS添加django_crontab  
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
    'app01.apps.App01Config',
]
```

* django-crontab配置  
django-crontab可以定时运行自定义命令和函数两种方式

i 定时函数  
在django项目的settings.py中添加以下命令  
    - 第一种的意思就是每一分钟执行一次你的定时函数  
    - 第二种时定时函数输出的内容到指定文件（如果该路径或文件不存在将会自动创建）
```
CRONJOBS = (
    ('*/1 * * * *', '你的app名.定时函数所在的py文件名.定时函数名'),
    ('0   0 1 * *', '你的app名.定时函数所在的py文件名.定时函数名', '> 输出文件路径和名称'),
)
```

ii 定时命令  
意思是在12点10分执行命令
```
CRONJOBS = (
    ('10 12 * * *', 'django.core.management.call_command', ['要执行的命令']),
)
```

## 定时任务的操作  
python manage.py crontab add　　添加定时任务  
python manage.py crontab remove 清除定时任务  
python manage.py crontab show 显示定时任务  
当你添加了或者修改的定时任务，只需执行命令1即可  
如果你想删除定时任务，请执行命令2  
  
- 注：
当定时任务执行时，如果你只是一些输出语句，那么你将看不到任何内容。请不要怀疑没有执行
上述环境在ubuntu16.04 lts django1.9中测试成功
上述文字皆为个人看法，如有错误或建议请及时联系我