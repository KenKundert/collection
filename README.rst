Collection
==========

| Version: 0.0.1
| Released: 2018-03-23
|

Collection is a class that provides a unified interface to various types of 
collections of data. Specifically, you can provide a list, a dictionary, a set, 
or a generator, and you can access the members of the collection as if they they 
were a in a list or a dictionary.

Consider the following collections:

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

List::

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

Dictionary::

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

Set::

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

Text::

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

Scalar::

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

Generator::

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

Indexing::

    >>> L[0]
    'alpha'

    >>> D['carol']
    '891-5810'

    >>> T[2]
    'mango'

    >>> G[1]
    1

Formatting::

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

Unfortunately, there seems to be an issue with f-strings. This example is 
virtually identical to the one above except that it uses f-strings. However, the 
above example works, but the following does not.

    >>> print(f'Email:\n    {C:{{v.name}} {{v.email}}|\n    }')
    Email:
        bob: bob@btca.com
        ted: ted@btca.com
        carol: carol@btca.com
        alice: alice@btca.com
