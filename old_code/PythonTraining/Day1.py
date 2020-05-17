Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

D:\PPT>cd python/hands

D:\PPT\python\hands>python
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [M
SC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more in
formation.
>>> a = 1
>>> type(a)
<class 'int'>
>>> f = 1.2
>>> type(f)
<class 'float'>
>>> s = "OK"
>>> type(s)
<class 'str'>
>>> a + 1
2
>>> print(aa)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'aa' is not defined
>>> a / 2
0.5
>>> a // 2
0
>>> a % 2
1
>>> a == 1
True
>>> a != 1
False
>>> b = True
>>> type(a)
<class 'int'>
>>> type(b)
<class 'bool'>
>>> a == 1 and a >= 1
True
>>> a == 1 or a >= 1
True
>>> not a == 1
False
>>> s = "1"
>>> type(s)
<class 'str'>
>>> a
1
>>> int(s)
1
>>> str(a)
'1'
>>> print(a)
1
>>> if a == 1:
...     print(a)
...
1
>>> if a == 1:
...     print(a)
...     print(a)
...     print(a)
...
1
1
1
>>> if a == 1:
...     print(a)
... else:
...     print(a)
...
1
>>> if a == 1:
...     print(a)
... elif a > 1:
...     print(a)
... else:
...     print(a)
...
1
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, fl
ush=False)

    Prints the values to a stream, or to sys.stdout by defau
lt.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the curr
ent sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a n
ewline.
    flush: whether to forcibly flush the stream.

>>> print(1,2,3,4)
1 2 3 4
>>> print(1,2,3,4, sep=":", end="***")
1:2:3:4***>>>
>>>
>>> s = "Hello"
>>> s = 'Hello'
>>> s = """Hello
... World"""
>>> s
'Hello\nWorld'
>>> s = "Hello"
>>> len(s)
5
>>> "H" in s
True
>>> "H" not in s
False
>>> s == "H"
False
>>> s != "H"
True
>>> for e in s:
...     print(e)
...
H
e
l
l
o
>>> s
'Hello'
>>> s[0]
'H'
>>> s[-len(s)]
'H'
>>> s[len(s)-1]
'o'
>>> s[-1]
'o'
>>> s[-len(s)]
'H'
>>> s = "Hello World"
>>> s[0:5]
'Hello'
>>> #start:end:step
...
>>> s[0:5:2]
'Hlo'
>>> s[::2]
'HloWrd'
>>> s[::-1]
'dlroW olleH'
>>> s[8:0:-1]
'roW olle'
>>>
>>> s = "Hello"
>>> s1 = s + " World"
>>> s1
'Hello World'
>>> s
'Hello'
>>> "OK" * 4
'OKOKOKOK'
>>> "%d %s %06.2" % (1,"OK", 2.3344)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: incomplete format
>>> "%d %s %06.2f" % (1,"OK", 2.3344)
'1 OK 002.33'
>>> s
'Hello'
>>> s[0]
'H'
>>> s[0] = 'K'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> s
'Hello'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__d
ir__', '__doc__', '__eq__', '__format__', '__ge__', '__getat
tribute__', '__getitem__', '__getnewargs__', '__gt__', '__ha
sh__', '__init__', '__iter__', '__le__', '__len__', '__lt__'
, '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '
__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setat
tr__', '__sizeof__', '__str__', '__subclasshook__', 'capital
ize', 'casefold', 'center', 'count', 'encode', 'endswith', '
expandtabs', 'find', 'format', 'format_map', 'index', 'isaln
um', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'isl
ower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'is
upper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'pa
rtition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition
', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> type(s)
<class 'str'>
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__d
ir__', '__doc__', '__eq__', '__format__', '__ge__', '__getat
tribute__', '__getitem__', '__getnewargs__', '__gt__', '__ha
sh__', '__init__', '__iter__', '__le__', '__len__', '__lt__'
, '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '
__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setat
tr__', '__sizeof__', '__str__', '__subclasshook__', 'capital
ize', 'casefold', 'center', 'count', 'encode', 'endswith', '
expandtabs', 'find', 'format', 'format_map', 'index', 'isaln
um', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'isl
ower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'is
upper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'pa
rtition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition
', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> s = "Hello World"
>>> help(str.split)
Help on method_descriptor:

split(...)
    S.split(sep=None, maxsplit=-1) -> list of strings

    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxspli
t
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.

>>> s.split(" ")
['Hello', 'World']
>>> s.split("w")
['Hello World']
>>> s.split("W")
['Hello ', 'orld']
>>> len(s)
11
>>> s.split("W)
  File "<stdin>", line 1
    s.split("W)
              ^
SyntaxError: EOL while scanning string literal
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__d
ir__', '__doc__', '__eq__', '__format__', '__ge__', '__getat
tribute__', '__getitem__', '__getnewargs__', '__gt__', '__ha
sh__', '__init__', '__iter__', '__le__', '__len__', '__lt__'
, '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '
__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setat
tr__', '__sizeof__', '__str__', '__subclasshook__', 'capital
ize', 'casefold', 'center', 'count', 'encode', 'endswith', '
expandtabs', 'find', 'format', 'format_map', 'index', 'isaln
um', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'isl
ower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'is
upper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'pa
rtition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition
', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> help(str.strip)
Help on method_descriptor:

strip(...)
    S.strip([chars]) -> str

    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in cha
rs instead.

>>> lt = [1, 2.3 , "OK", [1,2,3]]
>>> type(lt)
<class 'list'>
>>> list("OKY")
['O', 'K', 'Y']
>>> res = []
>>> type(res)
<class 'list'>
>>> len(lt)
4
>>> "OK" in lt
True
>>> "OK" not in lt
False
>>> lf == [1,2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lf' is not defined
>>> lt == [1,2]
False
>>> lt != [1,2]
True
>>> for e in lt:
...     print(e)
...
1
2.3
OK
[1, 2, 3]
>>> l
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l' is not defined
>>> lt
[1, 2.3, 'OK', [1, 2, 3]]
>>> lt[0]
1
>>> lt[-1]
[1, 2, 3]
>>> lt[-1] = 20
>>> lt
[1, 2.3, 'OK', 20]
>>> l2 = lt + [99,88]
>>> l2
[1, 2.3, 'OK', 20, 99, 88]
>>> lt
[1, 2.3, 'OK', 20]
>>> lt.append(20)
>>> lt
[1, 2.3, 'OK', 20, 20]
>>> lt += [23,34]
>>> lt
[1, 2.3, 'OK', 20, 20, 23, 34]
>>> lt += [300]
>>> lt
[1, 2.3, 'OK', 20, 20, 23, 34, 300]
>>> lt.append([20,56])
>>> lt
[1, 2.3, 'OK', 20, 20, 23, 34, 300, [20, 56]]
>>> del lt[2]
>>> lt
[1, 2.3, 20, 20, 23, 34, 300, [20, 56]]
>>>
>>>
>>> l = [1,2,3,4]
>>> res = [1,4,9,16]
>>> 3 * 3
9
>>> res = []
>>> for e in l:
...     res.append(e*e)
...
>>> print(res)
[1, 4, 9, 16]
>>>
>>>
>>> l = [1,2,3,4]
>>> res = [1,3]
>>> 2 % 2 == 0
True
>>> 3 % 2 == 0
False
>>> l = [1,2,3,4]
>>> res = [1,9]
>>> res = []
>>> for e in l:
...     if e % 2 == 1:
...             res.append(e*e)
...
>>>
>>>
>>>
>>>
>>> l = list(range(10))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l = list(range(3,20,2))
>>> l
[3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> l = list(range(5))
>>> l
[0, 1, 2, 3, 4]
>>> l + [22,33]
[0, 1, 2, 3, 4, 22, 33]
>>> l
[0, 1, 2, 3, 4]
>>> l * 4
[0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

>>> l[0]
0
>>> l[-1]
4
>>> l[0:3:1]
[0, 1, 2]
>>> l[0:3:2]
[0, 2]
>>> l[::2]
[0, 2, 4]
>>> l
[0, 1, 2, 3, 4]
>>> l[::-1]
[4, 3, 2, 1, 0]
>>> l
[0, 1, 2, 3, 4]
>>> l[-1] = 50
>>> l
[0, 1, 2, 3, 50]
>>> l[:0] = [99,88]
>>> l
[99, 88, 0, 1, 2, 3, 50]
>>> l[len(l):] = [66,77]
>>> l
[99, 88, 0, 1, 2, 3, 50, 66, 77]
>>> l[2:2] = [44,55]
>>> l
[99, 88, 44, 55, 0, 1, 2, 3, 50, 66, 77]
>>> l[2:3] = [24,35]
>>> l
[99, 88, 24, 35, 55, 0, 1, 2, 3, 50, 66, 77]
>>> l[0:5] = ["OK"]
>>> l
['OK', 0, 1, 2, 3, 50, 66, 77]
>>> l = list(range(5))
>>> l = [1,2,3]
>>> c = 0
>>> while c < 3:
...     l = [l]
...     c = c+1
...
>>> l
[[[[1, 2, 3]]]]
>>> type(l)
<class 'list'>
>>> len(l)
1
>>> l[0]
[[[1, 2, 3]]]
>>> type(l[0])
<class 'list'>
>>> len(l[0])
1
>>> l[0][0]
[[1, 2, 3]]
>>> type(l[0][0])
<class 'list'>
>>> len(l[0][0])
1
>>> l[0][0][0]
[1, 2, 3]
>>> l[0][0][0][2] = 30
>>> l
[[[[1, 2, 30]]]]
>>> l = [1,2,4]
>>> l = [1,1,1]
>>> l
[1, 1, 1]
>>>
>>> l
[1, 1, 1]
>>> s = set(l)
>>> s
{1}
>>> t = (1,2,3,4)
>>> len(t)
4
>>> 3 in  t
True
>>> 3 not in  t
False
>>> t == (1,3,4)
False
>>> for e in t:
...     print(e)
...
1
2
3
4
>>> t
(1, 2, 3, 4)
>>> t[0]
1
>>> t[0] = 30
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t[::-1]
(4, 3, 2, 1)
>>> t
(1, 2, 3, 4)
>>> t.append(30)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> t2 = t + (5,6)
>>> t2
(1, 2, 3, 4, 5, 6)
>>> t
(1, 2, 3, 4)
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__
doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getit
em__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__',
 '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__red
uce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__siz
eof__', '__str__', '__subclasshook__', 'count', 'index']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribu
te__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '_
_init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne_
_', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed_
_', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
 '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'in
dex', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(list.insert)
Help on method_descriptor:

insert(...)
    L.insert(index, object) -- insert object before index

>>> help(list.reverse)
Help on method_descriptor:

reverse(...)
    L.reverse() -- reverse *IN PLACE*

>>> ()
()
>>> type( () )
<class 'tuple'>
>>> type( (1) )
<class 'int'>
>>> type( (1,) )
<class 'tuple'>
>>> type( (1,2) )
<class 'tuple'>
>>>
>>> s = {1,2,3,4,1,2,3}
>>> s
{1, 2, 3, 4}
>>> s = {4,2,1,3}
>>> s
{1, 2, 3, 4}
>>> len(s)
4
>>> 3 in s
True
>>> 3 not in s
False
>>> s
{1, 2, 3, 4}
>>> s == { 2,3,1,4}
True
>>> for e in s:
...     print(e)
...
1
2
3
4
>>> s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>> s.append(20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'append'
>>> s.add(20)
>>> s
{1, 2, 3, 4, 20}
>>> s + {2,3}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>>
>>>
>>> {100,2,1,0,500}
{0, 1, 2, 500, 100}
>>> s1 = {1,2,3}
>>> s2 = {3,4,5}
>>> s1 | s2
{1, 2, 3, 4, 5}
>>> s1 & s2
{3}
>>> s1 - s2
{1, 2}
>>> s1 ^ s2
{1, 2, 4, 5}
>>> (s1-s2) | (s2-s1)
{1, 2, 4, 5}
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__
doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__'
, '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__
', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__
or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__
', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__
sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'differ
ence', 'difference_update', 'discard', 'intersection', 'intersection_u
pdate', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symm
etric_difference', 'symmetric_difference_update', 'union', 'update']
>>>
>>> s = "OK"
>>> sr = r"OK"
>>> su = u"OK"
>>> sb = b"OK"
>>> type(sr), type(su), type(sb)
(<class 'str'>, <class 'str'>, <class 'bytes'>)
>>> len("\n")
1
>>> len(r"\n")
2
>>> s
'OK'
>>> s.encode("utf-8")
b'OK'
>>> sb.decode("utf-8")
'OK'
>>> dir(bytes)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__
doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getit
em__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__',
 '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new
__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__'
, '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capital
ize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', '
fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', '
maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpart
ition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'stri
p', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__
doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getit
em__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__',
 '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new
__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__'
, '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capital
ize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs
', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isd
ecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintab
le', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstri
p', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', '
rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> set(dir(bytes)) - set(dir(str))
{'hex', 'fromhex', 'decode'}
>>> set(dir(str)) - set(dir(bytes))
{'isprintable', 'encode', 'isnumeric', 'casefold', 'format', 'isdecima
l', 'isidentifier', 'format_map'}
>>> s1
{1, 2, 3}
>>> s2
{3, 4, 5}
>>> s1 - s2
{1, 2}
>>> s2 - s1
{4, 5}
>>> (s1-s2) | (s2-s1)
{1, 2, 4, 5}
>>> s1 ^ s2
{1, 2, 4, 5}
>>> [{1,2} , {3,4}]
[{1, 2}, {3, 4}]
>>> {[1,2]  , [2,1] }
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> {1,2,3,1,2}
{1, 2, 3}
>>> hash(1)
1
>>> hash("OK")
-1597008304277431852
>>> hash("OK")
-1597008304277431852
>>> hash((1,2))
3713081631934410656
>>> hash((2,1))
3713082714465905806
>>> hash([2,1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> {(1,2)  , (2,1) }
{(1, 2), (2, 1)}
>>>






















































