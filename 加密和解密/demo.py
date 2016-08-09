加密分为可逆和非可逆性：

当我们要验证输入参数是否一致可以用非可逆性，通过md5密码串进行比对：
应用场景：
用户密码加密存入数据库，登录时候通过md5密码串进行比对（hashlib）

可逆的：
当加密时候我们需要提取数据二次应用时候使用可逆性(base64)

>>> import base64
>>> a = base64.b64encode("xiaoluo")
>>> a
'eGlhb2x1bw=='
>>> base64.b64decode('eGlhb2x1bw==')
'xiaoluo'


非可逆性：
>>> import hashlib
>>> a = hashlib.md5("xiaoluo")
>>> a
<md5 HASH object @ 0x7fba05f1c7c8>
>>> a.hexdigest()
'4bf2c7b90b12006ebd152632dfd0ca12'
>>> a = hashlib.md5("xiaoluo")
>>> a
<md5 HASH object @ 0x7fb9ffc14390>
>>> a.hexdigest()
'4bf2c7b90b12006ebd152632dfd0ca12'


