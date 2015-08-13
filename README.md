# 合作开发须知
1，目前已清除多余分支；<br>
2，需要保证master分支的绝对稳定，除组长外不允许其他人直接合并修改到master分支，更不允许合并后推送到远程库；<br>
3，大家干活都在已经存在的dev分支下，也就是说大家需要在dev分支下面建立各自的分支，需要提交时合并到dev分支再提交；<br>
4，开发环境统一用virtualenv搭建，具体需要安装模块参考[requirement.txt](https://github.com/maizi-stu-002/maizi-stu-002-project/blob/master/requirement.txt)，可切换到虚拟环境目录，使用命令pip install -r requirement快速安装相应模块；<br>
5，目前已对各自负责模块进行了功能拆分，主要拆分了views.py, urls.py和templates，大家各司其职即可。
