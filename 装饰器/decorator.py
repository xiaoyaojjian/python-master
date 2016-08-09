#/usr/bin/env python
#coding:utf-8


#  修饰器:相当于一个商标厂，任何一个产品生成完成后，都需要到修饰器里贴一下商标才能使用,将自己生成好的产品，送到商标处，商标厂商给贴商标

"""
#不传参数调用装饰器
def hello(fn):     #美国苹果公司 VS  验证谁有资格来增删改查
    def wrapper():
        print"hello, %s" % fn.__name__  #返回函数名，会返回传入的函数名 foo
        fn()                             # abc()     执行传来的函数foo并返回函数结果，不执行也行，它仅是wrappr的一个参数
        print"goodby, %s" % fn.__name__
    return wrapper                      
 
@hello
def abc():   #中国富士康 VS  数据的增删改查
    print"i am abc"
  
abc()
###fn 等于abc（）
"""

"""
hello, abc
i am abc
goodby, abc

"""
"""
#调用函数传参给装饰器
def fuck(fn):
    def wrapper(*arg,**args):                #接受回调函数的不定长参数。无论是*arg列表类型，还是**args字典类型 都识别
        print  "fuck %s!" % fn.__name__
        fn(*arg,**args)                     #return   fn(*arg,**args)    效果一样
    return wrapper

@fuck
def wfg(name):
    print "hello %s" % name 

wfg('cjk')
print wfg.__name__
"""
"""
fuck wfg!
hello cjk
wrapper

"""

#1：调用子函数给装饰器传参，2：装饰器也给调用子函数传参
def hello(fn):
    def wrapper(*args,**kwargs):
        print "hello, %s" % fn.__name__

        user = {'name':'lzp','age':18,'email':'lzp@126.com'}
        return fn(user,*args,**kwargs)    #一次只能返回一个参数，此处返回字典参数
    return wrapper

@hello
def foo(test,a):  #可以同时接受其他形式的参数，但接受装饰器的参数必须在前面 
   print "my name is son parages %s" % a
   print "i am %s,my email is %s" % (test['name'],test['email'])  #打印字典的返回值，结果：i am lzp,my email is lzp@126.com

#foo()
foo("fuck")

"""
#test 是接收装饰器的传参,a 是往函数传参

hello, foo
my name is son parages fuck
i am lzp,my email is lzp@126.com
"""





