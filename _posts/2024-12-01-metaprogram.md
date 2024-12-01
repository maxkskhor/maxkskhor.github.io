---
layout: post
title: "Metaprogramming in Python"
date: 2024-12-01 21:13:00 +0000
categories: python notes
permalink: /notes/python/metaprogramming
---

> "In computer programming jargon, a heisenbug is a software bug that seems to disappear or alter its behavior when one attempts to study it."
>
> Wikipedia



### Attributes
1. Python objects have _attributes_, which could be data or a _callable_ (a.k.a. a method).
2. **Dynamic attributes** look the same as data attributes (i.e. `obj.x`) but the difference is when you actually 'dot x', some underlying computations happen on demand.

### The `__slots__` method
1. Python stores the attributes of each instance in a `dict` named `__dict__`, unless the class attribute `__slots__` is defined.
2. The `__slots__` is more memory efficient because it does not allow additional attributes to be set.
{% highlight python %}
# simple example
class A:
    __slots__ = ('x', 'y')

>>> a = A()
>>> a.__dict__
AttributeError: 'A' object has no attribute '__dict__'

>>> a.x = 5
>>> a.y = 6
>>> a.z = 10
AttributeError: 'A' object has no attribute 'z'
{% endhighlight %}

### The `__new__` method
{% highlight python %}
# how __new__ is actually called during object creation
def construct(the_class, init_args):
    new_object = the_class.__new__(init_args)
    if isinstance(new_object, the_class):
        the_class.__init__(new_object, init_args)
return new_object
{% endhighlight %}


