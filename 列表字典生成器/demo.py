列表推倒式生成列表:

1、单循环列表生成
>>> [x for x in 'abc']
['a', 'b', 'c']

2、双循环，两个嵌套执行:
>>> [m + n for m in 'abc' for n in 'ABC']
['aA', 'aB', 'aC', 'bA', 'bB', 'bC', 'cA', 'cB', 'cC']

>>> [m + n for m in '123' for n in '456']   
['14', '15', '16', '24', '25', '26', '34', '35', '36']

3、加if判断的列表生成式
>>> [x*x for x in range(1,11) if x%2 ==0]
[4, 16, 36, 64, 100]

4、字典迭代生成
>>> field=[k for k,v in d.items()] 
>>> value=[v for k,v in d.items()] 
>>> field
['age', 'name', 'sex']

>>> d = {'x': 'A', 'y': 'B', 'z': 'C'}  
>>> [k + '=' + v for k,v in d.items()]
['y=B', 'x=A', 'z=C']


二、字典生成式:
>>> list = ['wd','18','nan']
>>> dict((k,v) for k,v in enumerate(list))
{0: 'wd', 1: '18', 2: 'nan'}
#按位置生成字典

2、flask 应用
fields=['id','name','age'] #数据表的列
result_set = self.fetchone() #结果是一个单元组
dict([(k, result_set[i]) for i,k in enumerate(fields)]

3、元组列表生成式：
>>> a = ((1,'ab'),(2,'bc'))
>>> dict(a)
{1: 'ab', 2: 'bc'}

>>> a = [[1,'ab'],[2,'bc']]
>>> dict(a)
{1: 'ab', 2: 'bc'}

