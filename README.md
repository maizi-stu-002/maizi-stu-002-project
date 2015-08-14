# 合作开发须知
1，为保证master分支的绝对稳定，除组长和副组长外不允许其他人直接合并修改到master分支，更不允许合并后推送到远程库；<br>
2，大家需要在dev分支下面建立各自的分支，需要提交时合并到dev分支再提交；<br>
3，开发环境统一用virtualenv搭建，具体需要安装模块参考[requirement.txt](https://github.com/maizi-stu-002/maizi-stu-002-project/blob/master/requirement.txt)，可切换到虚拟环境目录，使用命令pip install -r requirement.txt快速安装相应模块；<br>
4，目前已对各自负责模块进行了功能拆分，主要拆分了views.py, urls.py和templates，大家各司其职即可;<br>
##2015-08-15更新
1，models和admin初步完成，程序能初步运行；<br>
2，为避免models和admin过于凌乱，建议大家不要直接修改这两个文件，发现问题或确认要修改，告知组长或副组长，由组长或副组长统一修改。
