#!/usr/bin/env python
#coding=utf8


s = '{0},{1}'.format('Cedar', 20)
print s  # Cedar,20

s = '{},{}'.format('Cedar', 20)  # we can ignore the number
print s  # Cedar,20

# access through keys
s = '{name},{age}'.format(age=20, name='Cedar')
print s

p = {'name':'Cedar', 'age':20}
p = '{name},{age}'.format(**p)
print p

# access through attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Cedar', 20)
s = '{person.name},{person.age}'.format(person=p)
print s

# access through index
p = ['Cedar', 20]
s = '{0[0]},{0[1]}'.format(p)
print s

# Alignment - center:^, left:<, right:> - followed by width
# {:[filling char][^,<,>][width]}

# alignment to the left, width is 4, filling characters is ' ' (default)
s = '|{:<4}|'.format(8)
print s

# alignment to the right, width is 4, filling characters is '0'
s = '|{:0>4}|'.format(8)
print s

# alignment to the center, width is 4, filling characters is '0'
s = '|{:0^4}|'.format(8)
print s  # 0800

# precision for floating number
s = '{:.2f}'.format(3.1415926)
print s  # 3.14

s = '{:.2f}'.format(3.1455926)
print s  # 3.15

s = '{:.2f}'.format(1)
print s  # 1.00

# binary: b, octal: o, hex: x, decimal: d
print '{:b}'.format(17)
print '{:o}'.format(17)
print '{:x}'.format(17)
print '{:d}'.format(17)

# readable large number
print '{:,}'.format(123456789)  # 123,456,789
