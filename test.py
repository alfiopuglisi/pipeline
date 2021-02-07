#!/usr/bin/env python

import types

from pipeline import p


# Simplest
assert 'foo' >> p.len == 3

# Builtins replacement
assert range(10) >> p.filter(lambda i : i%2) >> p.map(lambda i : i*i) >> p.list == [1, 9, 25, 49, 81]

# Lambda
assert 'foo' >> p(lambda x: x.upper()) == 'FOO'

# Function object
assert 'foo' >> p('The word was {}'.format) == 'The word was foo'

# Chained generators results in generator
assert type(range(10) >> p(x*2 for x in p.value if x%2==0)  >> p(x*3 for x in p.value)) == types.GeneratorType

# Generator execution
assert range(10) >> p(x*2 for x in p.value if x%2==0)  >> p(x*3 for x in p.value) >> p.list == [0, 12, 24, 36, 48]


# Imported functions via globals()

from re import findall
from pipeline import Pipeline

p = Pipeline(globals())

s = '<a href="a">a</a> <a href="b">b</a>'
assert s >> p.findall('href="') >> p.len >> p('{} hrefs'.format) == '2 hrefs'
