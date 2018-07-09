fortify审计
=========

1. 利用fortify 命令行进行代码审计，并且把审计结果入库并转换为Pdf
2. 目前除前端页面外其他基本完成
3. 属于废弃项目

## 部署情况

windows 线上服务器 192.168.x.x




## 安装

```
pip install django==1.8.0
pip install Mysql-python
# 如果mysql-python出错，安装https://pypi.python.org/pypi/MySQL-python/1.2.5 
pip install django-celery
pip install gittle
pip install dulwich=0.9.1
# __init__() got an unexpected keyword argument 'pkey'
# download dulwich https://github.com/AaronO/dulwich/tarball/eebb032b2b7b982d21d636ac50b6e45de58b208b#egg=dulwich-0.9.1-2
# python setup.py --pure install
# 这个dulwich少refs.py 文件
pip install django-bootstrap3 
```

## bug
### 拉取代码时git资源里存在特殊字符时会出现bug
```
2018-01-23 15:43:09,778: ERROR/MainProcess] Task fortifyaAudit.tasks.createTask[0d12f1ee-a9b0-45ea-ad60-5c4fe742f4ef] raised unexpected: UnicodeDecodeError('ascii', 'public/img/QQ\xe9\x8d\xa5\xe5\x89\xa7\xe5\xa2\x9620170406102530.png', 13, 14, 'ordinal not in range(128)')
Traceback (most recent call last):
  File "D:\Python27\lib\site-packages\celery\app\trace.py", line 240, in trace_task
    R = retval = fun(*args, **kwargs)
  File "D:\Python27\lib\site-packages\celery\app\trace.py", line 438, in __protected_call__
    return self.run(*args, **kwargs)
  File "D:\workspace\auditCode\fortifyaAudit\tasks.py", line 62, in createTask
    raise e
 ```
### 拉取代码时无更新不进行检测

### 某些项目处理时间超长

js文件建模问题

## 运行方式

```
# python2.7
python manage.py celery  worker -l info # 启动worker
```

## 遗留问题
- 前端展示漏洞调用过程和对应代码