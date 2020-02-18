Collection
==========

| Version: 0.2.1
| Released: 2020-02-18
|

Collection is a class that provides a unified interface to various types of 
collections of data. Specifically, you can provide a list, a dictionary, a set, 
or a generator, and you can access the members of the collection as if they they 
were a in a list or a dictionary. For collections like lists where there is no 
key, the index is used instead.

Consider the following collections::

    >>> l = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    >>> d = dict(
    ...     bob='239-8402', ted='371-8567', carol='891-5810', alice='552-2219'
    ... )
    >>> s = {45, 27, 37, 22}
    >>> t = 'apple orange mango'
    >>> o = 'tooth'

Passing these to Collection allow you to treat them either as lists or as 
dictionaries::

    >>> from collection import Collection


Lists
-----

You can build a collection from a list. In this case the index is used as the 
key::

    >>> L = Collection(l)
    >>> for each in L:
    ...     print(each)
    alpha
    beta
    gamma
    delta
    epsilon

    >>> for each in L.values():
    ...     print(each)
    alpha
    beta
    gamma
    delta
    epsilon

    >>> for each in L.keys():
    ...     print(each)
    0
    1
    2
    3
    4

    >>> for k, v in L.items():
    ...     print(k, v)
    0 alpha
    1 beta
    2 gamma
    3 delta
    4 epsilon


Dictionaries
------------

You can build a collection from a dictionary::

    >>> D = Collection(d)
    >>> for each in D:
    ...     print(each)
    239-8402
    371-8567
    891-5810
    552-2219

    >>> for each in D.values():
    ...     print(each)
    239-8402
    371-8567
    891-5810
    552-2219

    >>> for each in D.keys():
    ...     print(each)
    bob
    ted
    carol
    alice

    >>> for k, v in D.items():
    ...     print(k, v)
    bob 239-8402
    ted 371-8567
    carol 891-5810
    alice 552-2219


Sets
----

You can build a collection from a set. In this case the index is used as the 
key::

    >>> S = Collection(s)
    >>> for each in S:
    ...     print(each)
    37
    27
    45
    22

    >>> for each in S.values():
    ...     print(each)
    37
    27
    45
    22

    >>> for each in S.keys():
    ...     print(each)
    0
    1
    2
    3

    >>> for k, v in S.items():
    ...     print(k, v)
    0 37
    1 27
    2 45
    3 22


Text
----

If you provide a string it will be split for form a list. You can specify the 
*splitter* string, but if you don't the string is split on white space. You can 
also specify *splitter=False*, in which case the string is not split (it is 
taken as a scalar::

    >>> T = Collection(t)
    >>> for each in T:
    ...     print(each)
    apple
    orange
    mango

    >>> for each in T.values():
    ...     print(each)
    apple
    orange
    mango

    >>> for each in T.keys():
    ...     print(each)
    0
    1
    2

    >>> for k, v in T.items():
    ...     print(k, v)
    0 apple
    1 orange
    2 mango

You can also specify a function as the splitter. The splitter must take a string 
as its first argument and return any of the supported collection types (list, 
dictionary, etc.). There is one splitter function provided: *split_lines*. It is 
used to convert multiline strings into lists.

    >>> transfers = '''
    ...     # January
    ...     $1,000     # from Bob
    ...      -$500     # to Ted
    ...
    ...     # February
    ...       $750     # from Carol
    ...     -$1250     # to Alice
    ... '''

    >>> from collection import Collection, split_lines

    >>> xfers = Collection(transfers, split_lines, cull=True, strip=True, comment='#')
    >>> for xfer in xfers:
    ...     print(xfer)
    $1,000
    -$500
    $750
    -$1250

Any named arguments that are unknown to *Collection* are passed on to the 
splitter function.  *split_lines* takes three named arguments: *comment* 
specifies each line should be partitioned with the given comment string and the 
comment string and whatever follows it should be removed, *cull* specifies that 
empty lines should be removed, and *split* specifies that each member of the 
list should be stripped of leading and trailing white space.


Scalar
------

You can build a collection from a single member. In this case the key is None::

    >>> O = Collection(o, splitter=False)
    >>> for each in O:
    ...     print(each)
    tooth

    >>> for each in O.values():
    ...     print(each)
    tooth

    >>> for each in O.keys():
    ...     print(each)
    None

    >>> for k, v in O.items():
    ...     print(k, v)
    None tooth


Generators
----------

You can build a collection from a generator. In this case the index is used as 
the key::

    >>> G = Collection(range(4))
    >>> for each in G:
    ...     print(each)
    0
    1
    2
    3

    >>> for each in G.values():
    ...     print(each)
    0
    1
    2
    3

    >>> for each in G.keys():
    ...     print(each)
    0
    1
    2
    3

    >>> for k, v in G.items():
    ...     print(k, v)
    0 0
    1 1
    2 2
    3 3


Indexing
--------

You can access the individual members of you collection using an index/key::

    >>> L[0]
    'alpha'

    >>> D['carol']
    '891-5810'

    >>> T[2]
    'mango'

    >>> G[-1]
    3


Formatting
----------

When formatting a collection you can specify a member format and a separator.  
These two things are specified in the format specifier for the collection 
argument. The format specifier has two parts separated by a bar (|) (this 
character can be changed by setting the collections ``splitter`` attribute).  
The part before the bar is a format string that is applied to each member in the 
collection. You can use {{k}} to interpolate the key and {{}}, {{0}}, or {{v}} 
to interpolate the value.  If the value has attributes, you can access them 
using something like {{v.attr}}. The part after the bar is the join string. It 
is placed between every member.  By default the join string is ', '.

::

    >>> print('Phone Numbers:\n    {:{{k}}: {{v}}|\n    }'.format(D))
    Phone Numbers:
        bob: 239-8402
        ted: 371-8567
        carol: 891-5810
        alice: 552-2219

    >>> class Info:
    ...     def __init__(self, **kwargs):
    ...         self.__dict__.update(kwargs)

    >>> C = Collection([
    ...     Info(name='bob', email='bob@btca.com'),
    ...     Info(name='ted', email='ted@btca.com'),
    ...     Info(name='carol', email='carol@btca.com'),
    ...     Info(name='alice', email='alice@btca.com'),
    ... ])

    >>> print('Email:\n    {}'.format(C.render('{v.name}: {v.email}', '\n    ')))
    Email:
        bob: bob@btca.com
        ted: ted@btca.com
        carol: carol@btca.com
        alice: alice@btca.com

    >>> print('Email:\n    {:{{v.name}}: {{v.email}}|\n    }'.format(C))
    Email:
        bob: bob@btca.com
        ted: ted@btca.com
        carol: carol@btca.com
        alice: alice@btca.com

Unfortunately, there seems to be an issue with f-strings (`bug report 
<https://bugs.python.org/issue39601>`_). This example is virtually identical to 
the one above except that it uses f-strings. However, the above example works, 
but the following does not.

    >>> print(f'Email:\n    {C:{{v.name}} {{v.email}}|\n    }')
    Traceback (most recent call last):
      ...
    AttributeError: 'int' object has no attribute 'name'

You can also set class or object attributes to control the formatting::

    >>> C.fmt = '{v.name}: {v.email}'
    >>> C.sep = '\n    '
    >>> print(f'Email:\n    {C}')
    Email:
        bob: bob@btca.com
        ted: ted@btca.com
        carol: carol@btca.com
        alice: alice@btca.com

If you take this approach, you can make ``fmt`` a function, in which case it it 
is called with positional arguments, ``k`` & ``v``, with the result expected to 
be a string that represents the formatted item::

    >>> C.fmt = lambda k, v: f'{v.name}: {v.email}'
    >>> C.sep = '\n    '
    >>> print(f'Email:\n    {C}')
    Email:
        bob: bob@btca.com
        ted: ted@btca.com
        carol: carol@btca.com
        alice: alice@btca.com
