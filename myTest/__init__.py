#如果没有__init__.py文件的话就是普通的directory，它就不能被导入或者包含其它的模块和嵌套包，那么执行也是无效的。
#所以说 __init__.py的 第一个作用就是package的标识。
#如果是直接新建 python package 的话，可以看到会默认在该目录下新增一个 __init__.py 文件，该Python文件默认是空的。

#__init__.py作用
#1. python中package的标识，它可以什么也不定义；可以只是一个空文件，但是必须存在，不能删除。
#2. 我们可以在__init__.py导入我们需要的模块，不需要一个个导入了。
#3. __init__.py 中还有一个重要的变量，__all__, 它用来将模块全部导入。

# __init__.py  中将模块全部导入
# __all__ =['os', 'sys', 're', 'urllib']
# a.py 中可使用 import* 直接导入
# from package import*
