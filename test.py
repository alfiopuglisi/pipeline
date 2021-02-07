
from pipeline import p


assert 'foo' >> p.len == 3

assert range(10) >> p.filter(lambda i : i%2) >> p.map(lambda i : i*i) >> p.list == [1, 9, 25, 49, 81]

assert 'foo' >> p(lambda x: x.upper()) == 'FOO'

assert 'foo' >> p('The word was {}'.format) == 'The word was foo'

assert range(10) >> p(x*2 for x in p.value if x%2==0)  >> p(x*3 for x in p.value) >> p.list == [0, 12, 24, 36, 48]


from re import findall
from pipeline import Pipeline

p = Pipeline(globals())

s = '<a href="a">a</a> <a href="b">b</a>'
assert s >> p.findall('href="') >> p.len >> p('{} hrefs'.format) == '2 hrefs'
