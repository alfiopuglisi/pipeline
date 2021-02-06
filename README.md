# pipeline

Module for pipelining composition.

Tired of

```python
func3(func2(func1(value)))
```
which must be read right-to-left? How about:

```python
value >> func1 >> func2 >> func3 ...
```

Pipelines are expressions whose resulting value can be assigned:

```python
result = value >> func1 >> func2 >> func3
```

Rules:
 * First value can be any python value
 * Functions must be chained with the '>>' operator.
 * All functions must be built as attributes of a Pipeline object and must accept
    one argument, that will be set using the pipelined value.
    Any additional arguments must be specified in the pipeline and the value will be added
    as the last argument.

Examples:
```python
from pipeline import p

# This pipeline has a result of 3
'foo' >> p.len

# This pipeline chains filters and maps objects, and calls list() on them
# at the end to execute them. The result will be [1, 9, 25, 49, 81]

range(10) >> p.filter(lambda i : i%2) >> p.map(lambda i : i*i) >> p.list

# If you already have a function object (or want to define one with lambda),
# pass it as a parameter to p():

range(10) >> p(lambda x: x*2)
'foo' >> p('The word was {}'.format)

# if imported symbols are used, they must be passed
# to the Pipeline constructor. This example counts
# the links in the python.org page, but since 'findall'
#'is imported, we must build a Pipeline object using
# the globals() array:

from pipeline import Pipeline
from urllib.request import urlopen
from re import findall

p = Pipeline(globals())
url = 'http://python.org'
urlopen(url).read() >> p.findall(b'href="') >> p.len >> p('{} hrefs'.format)
 ```
With special thanks to https://mtomassoli.wordpress.com/2012/03/29/pipelining-in-python/ who inspired this project.
