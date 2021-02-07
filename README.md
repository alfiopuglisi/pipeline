# pipeline

Module for pipelining composition.

Tired of

```python
func3(func2(func1(value)))
```
which must be read right-to-left? How about:

```python
value >> func1 >> func2 >> func3
```

Pipelines are expressions whose resulting value can be assigned:

```python
result = value >> func1 >> func2 >> func3
```

Rules:
 * First value can be any python value
 * Functions must be chained with the '>>' operator.
 * Functions are called as attributes of a Pipeline object (see the examples). All built-in functions are available. User-defined or imported functions must be passed to the Pipeline object constructor as a dictionary, typically using locals() or globals().
 * All functions must accept one argument, that will be set using the pipelined value.
    Any additional arguments must be specified in the pipeline and the value will be added
    as the last argument.
 * Generators are allowed. Using a generator will turn the value being pipelined in a generator object, meaning that subsequent pipeline steps must be able to consume the values (for example with p.list). Multiple generators will be automatically chained, and if the last step is a generator, the whole expression becomes a single generator ready for action!

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

'foo' >> p(lambda x: x.upper())
'foo' >> p('The word was {}'.format)

# if imported symbols are used, they must be passed
# to the Pipeline constructor. This example counts
# the links in the python.org page, but since 'findall'
# is imported, we must build a Pipeline object using
# the globals() array:

from pipeline import Pipeline
from urllib.request import urlopen
from re import findall

p = Pipeline(globals())
url = 'http://python.org'
urlopen(url).read() >> p.findall(b'href="') >> p.len >> p('{} hrefs'.format)

# Generator support using the special "p.value" keyword:

range(10) >> p(x*2 for x in p.value if x%2==0)  >> p(x*3 for x in p.value)

# The result will be a generator, that is, nothing is executed until
# the final generator will be asked to produce the values!

```
With special thanks to https://mtomassoli.wordpress.com/2012/03/29/pipelining-in-python/ who inspired this project.
