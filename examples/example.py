#!/usr/bin/env python
'''Simple example, only using builtins'''

from pipeline import p

range(10) >> p.filter(lambda i : i%2) >> p.map(lambda i : i*i) >> p.list >> p.print

a = range(10) >> p.filter(lambda i : i%2) >> p.map(lambda i : i*i) >> p.list

print(a)


from urllib.request import urlopen
from re import findall

from pipeline import Pipeline

p = Pipeline(globals())

url = 'http://python.org'

urlopen(url).read() >> p.findall(b'href="') >> p.len >> p('{} hrefs'.format) >> p.print

urlopen(url) >> p(lambda x: x.read()) >> p.findall(b'href="') >> p.len >> p('{} hrefs'.format) >> p.print
