合作开发须知
===========

####2015-08-21更新
* `models.py`已做修改，注释了绝大部分LPS相关表单，添加了首页需要的`战略合作`、`友情链接`和`推荐阅读`表单，`admin.py`做了相应调整。另外，
    有对部分表单字段进行增删改动作，都是根据实际需要做出的微调，请各位留意。
* 如果方便，大家尽量从`templates`下面的`base.html`继承，可以减少冲突，如果一定要用自己定制的模板，需确保不会干扰他人正常继承`base.html`。

####2015-08-15更新
* `models.py`和`admin.py`已初步完成,为避免冲突过多，不建议大家直接修改这两个文件，若确认要修改，可告知组长或副组长，由组长或副组长统一修改。
* `base.html`模板修改完成，置于`templates`根目录，大家根据自身需求选择继承即可。

####2015-08-13更新
* 为保证`master`分支的绝对稳定，除组长和副组长外不允许其他人直接合并修改到`master`分支，更不允许合并后推送到远程库。
* 为便于代码管理，大家需要在`dev`分支下面建立各自的分支，需要提交到远程库时先合并到`dev`分支再提交。
* 开发环境统一用`virtualenv`搭建，具体需要安装模块参考[requirement.txt](https://github.com/maizi-stu-002/maizi-stu-002-project/blob/master/requirement.txt )，
    可切换到虚拟环境目录，使用命令`pip install -r requirement.txt`快速安装相应模块。
* 目前已对各自负责模块进行了功能拆分，主要拆分了`views.py`, `urls.py`和`templates`，大家各司其职即可。

