# django

一、环境搭建
	1.python2.7以上
	
	2.django模块
  windows下安装
	pip --default-timeout=100 install -U Django==1.11.7
  
  liunx下安装django
    http://www.cnblogs.com/freeweb/p/5210167.html
	
	3.sqlite3工具 SQLite Expret Personal
	
二、创建项目	
	
	1.创建步骤
		打开命令行，进入想要安置项目的目录
		命令行输入：django-admin startproject myblog
		若没有报错，则创建项目成功
	
	2.启动命令
		python manange.py runserver
		python manange.py runserver 9999 （换端口）
	
	3.生成的目录介绍		
		myblog目录
			项目的一个容器、包含项目最基本的一些配置、目录名称不建议修改
		
		wsgi.py
			WSGI(Python Web Sever Gateway Interface)Python服务器网关接口
			python应用与Web服务器之间的接口
		
		urls.py
			URL配置文件
			django项目中所有地址（页面）都需要我们自己去配置其URL
		
		settings.py
			项目总配置文件
			里面包含了数据库、Web应用、时间等各种配置
			# SECURITY WARNING: don't run with debug turned on in production!
			DEBUG = True
			ALLOWED_HOSTS = []
			ALLOWED_HOSTS = ['localhost'] 只允许以localhost访问
		
		__init__.py
			Python中声明模块的文件
			内容默认为空
			
三、创建应用

		1.创建步骤
			打开命令行，进入项目中manage.py所在的目录
			
			命令行输入：django manange.py startapp blog
			
			添加应用名到settings.py 中的INSTALLED_APPS里
			
			注意:不能和python模块名相同
			
		2.新建应用中各文件意义
			migrations
				数据移植（迁移）模块
				内容自动生成
				
			admin.py
				该应用的后台管理系统配置
				
			apps.py
				该应用的一些配置
				Django-1.9以后自动生成
				
			models.py
				数据模块
				使用ORM框架
				类似MVC结构中的Models（模型）
				
			test.py
				自动化测试模块
				Django提供了自动化测试功能
				在这里编写测试脚本（语句）
				
			views.py
				执行响应代码所在的模块
				代码逻辑处理的主要地点
				项目中大部分代码均在这里编写
			
			
			
			
	
	
	