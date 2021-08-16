## 黑白名单 基于django-simpleui+django+python 实现


### 原理

-  拉取 小曾的黑白名单数据（https://www.zengjie.top/public/company/search） 同步到数据库中
-  在simpleui中显示，查询，编辑等


### 使用
- 下载源码
- 创建mysql数据库bw_list 查看setting文件数据库信息是否一致
- 应用python manger.py makemigrations x; python manger.py migrate x
- 执行init_sql.py文件 python init_sql.py # 生成最新数据，执行完成后查看数据库是否有数据
- 设置项目虚拟环境venv，并执行pip -r install requirements.txt
- 创建超级用户 python manger createsuperuser。使用该用户登录 /admin
- 启动项目 python manger.py runserver 8000 进入http://127.0.0.1/admin