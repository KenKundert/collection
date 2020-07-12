# encoding: utf8

from collection import Collection, split_lines
import pytest
from textwrap import dedent

def test_empty():
    N = Collection(None)

    assert list(N) == []
    assert list(m for m in N) == []
    assert N.values() == []
    assert N.keys() == []
    assert N.items() == []
    assert len(N) == 0
    assert 'upsilon' not in N
    with pytest.raises(IndexError) as exception:
        N[0]
    assert str(exception.value) == 'list index out of range'

def test_list():
    l = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    L = Collection(l)

    assert list(L) == l
    assert list(m for m in L) == l
    assert L.values() == l
    assert L.keys() == list(range(len(l)))
    assert L.items() == [(k, v) for k,v in zip(range(len(l)), l)]
    assert len(L) == len(l)
    assert 'alpha' in L
    assert 'beta' in L
    assert 'gamma' in L
    assert 'delta' in L
    assert 'epsilon' in L
    assert 'upsilon' not in L
    assert L[0] == 'alpha'
    assert L[1] == 'beta'
    assert L[2] == 'gamma'
    assert L[3] == 'delta'
    assert L[4] == 'epsilon'
    assert L[-1] == 'epsilon'
    assert L[-2] == 'delta'
    assert L[-3] == 'gamma'
    assert L[-4] == 'beta'
    assert L[-5] == 'alpha'
    with pytest.raises(IndexError) as exception:
        L[5]
    assert str(exception.value) == 'list index out of range'

def test_dict():
    d = dict(
        bob='239-8402', ted='371-8567', carol='891-5810', alice='552-2219'
    )
    D = Collection(d)
    assert list(D) == list(d.values())
    assert list(m for m in D) == list(d.values())
    assert D.values() == list(d.values())
    assert D.keys() == list(d.keys())
    assert D.items() == list(d.items())
    assert len(D) == len(d)
    assert '239-8402' in D
    assert '371-8567' in D
    assert '891-5810' in D
    assert '552-2219' in D
    assert '747-7658' not in D
    assert D['bob'] == '239-8402'
    assert D['ted'] == '371-8567'
    assert D['carol'] == '891-5810'
    assert D['alice'] == '552-2219'
    with pytest.raises(KeyError) as exception:
        D['jeff']
    assert str(exception.value) == "'jeff'"

def test_set():
    s = {45, 27, 37, 22}
    S = Collection(s)
    assert set(S) == s
    assert set(m for m in S) == s
    assert set(S.values()) == s
    assert S.keys() == list(range(len(s)))
    for i, m in enumerate(S.items()):
        k, v = m
        assert k == i
        assert v in s
    assert len(S) == len(s)
    assert 45 in S
    assert 27 in S
    assert 37 in S
    assert 22 in S
    assert 99 not in S
    with pytest.raises(TypeError) as exception:
        S[5]
    assert str(exception.value) == "'set' object is not subscriptable"

def test_text_no_split():
    t = 'apple orange mango'
    T = Collection(t, False)

    assert list(T) == [t]
    assert list(m for m in T) == [t]
    assert T.values() == [t]
    assert T.keys() == [None]
    assert T.items() == [(None, t)]
    assert len(T) == 1
    assert 'apple orange mango' in T
    assert 'apple' not in T
    assert 'orange' not in T
    assert 'mango' not in T
    assert T[None] == 'apple orange mango'
    with pytest.raises(KeyError) as exception:
        T[2]
    assert str(exception.value) == '2'

def test_text_smpl():
    t = 'apple orange mango'
    T = Collection(t)
    l = t.split()

    assert list(T) == l
    assert list(m for m in T) == l
    assert T.values() == l
    assert T.keys() == list(range(len(l)))
    assert T.items() == [(k, v) for k,v in zip(range(len(l)), l)]
    assert len(T) == len(l)
    assert 'apple' in T
    assert 'orange' in T
    assert 'mango' in T
    assert 'upsilon' not in T
    assert T[0] == 'apple'
    assert T[1] == 'orange'
    assert T[2] == 'mango'
    assert T[-1] == 'mango'
    assert T[-2] == 'orange'
    assert T[-3] == 'apple'
    with pytest.raises(IndexError) as exception:
        T[5]
    assert str(exception.value) == 'list index out of range'

def test_text_splitter_smpl():
    t = 'apple\norange\nmango'
    T = Collection(t, split_lines)
    l = t.split()

    assert list(T) == l
    assert list(m for m in T) == l
    assert T.values() == l
    assert T.keys() == list(range(len(l)))
    assert T.items() == [(k, v) for k,v in zip(range(len(l)), l)]
    assert len(T) == len(l)
    assert 'apple' in T
    assert 'orange' in T
    assert 'mango' in T
    assert 'upsilon' not in T
    assert T[0] == 'apple'
    assert T[1] == 'orange'
    assert T[2] == 'mango'
    assert T[-1] == 'mango'
    assert T[-2] == 'orange'
    assert T[-3] == 'apple'
    with pytest.raises(IndexError) as exception:
        T[5]
    assert str(exception.value) == 'list index out of range'


def test_text_splitter():
    t = transfers = '''
        # January
        $1,000     # from Bob
         -$500     # to Ted

        # February
          $750     # from Carol
        -$1250     # to Alice
    '''
    T = Collection(t, split_lines, cull=True, strip=True, comment='#')
    l = ['$1,000', '-$500', '$750', '-$1250']

    print(list(T))
    assert list(T) == l
    assert list(m for m in T) == l
    assert T.values() == l
    assert T.keys() == list(range(len(l)))
    assert T.items() == [(k, v) for k,v in zip(range(len(l)), l)]
    assert len(T) == len(l)
    assert '$1,000' in T
    assert '-$500' in T
    assert '$750' in T
    assert '-$1250' in T
    assert 'upsilon' not in T
    assert T[0] == '$1,000'
    assert T[1] == '-$500'
    assert T[2] == '$750'
    assert T[3] == '-$1250'
    assert T[-1] == '-$1250'
    assert T[-2] == '$750'
    assert T[-3] == '-$500'
    assert T[-4] == '$1,000'
    with pytest.raises(IndexError) as exception:
        T[5]
    assert str(exception.value) == 'list index out of range'

def test_generator():
    L = Collection(range(5))
    l = list(range(5))

    assert list(L) == l
    assert list(m for m in L) == l
    assert L.values() == l
    assert L.keys() == list(range(len(l)))
    assert L.items() == [(k, v) for k,v in zip(range(len(l)), l)]
    assert len(L) == len(l)
    assert 0 in L
    assert 1 in L
    assert 2 in L
    assert 3 in L
    assert 4 in L
    assert 5 not in L
    assert L[0] == 0
    assert L[1] == 1
    assert L[2] == 2
    assert L[3] == 3
    assert L[4] == 4
    assert L[-1] == 4
    assert L[-2] == 3
    assert L[-3] == 2
    assert L[-4] == 1
    assert L[-5] == 0
    with pytest.raises(IndexError) as exception:
        L[5]
    assert str(exception.value) == 'range object index out of range'

def test_formatting():
    l = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    L = Collection(l)
    assert L.render() == 'alpha beta gamma delta epsilon'
    L.sep = ', '
    assert L.render() == 'alpha, beta, gamma, delta, epsilon'
    L.fmt = '<{v}>'
    assert L.render() == '<alpha>, <beta>, <gamma>, <delta>, <epsilon>'

    d = dict(
        bob='239-8402', ted='371-8567', carol='891-5810', alice='552-2219'
    )
    D = Collection(d)
    expected = 'bob: 239-8402, ted: 371-8567, carol: 891-5810, alice: 552-2219'
    assert D.render('{k}: {v}', ', ') == expected

    class Info:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    C = Collection([
        Info(name='bob', email='bob@btca.com'),
        Info(name='ted', email='ted@btca.com'),
        Info(name='carol', email='carol@btca.com'),
        Info(name='alice', email='alice@btca.com'),
    ])
    result1 = 'Email:\n    {}'.format(C.render('{v.name}: {v.email}', '\n    '))
    result2 = 'Email:\n    {:{{v.name}}: {{v.email}}|\n    }'.format(C)
    expected1 = dedent('''
        Email:
            bob: bob@btca.com
            ted: ted@btca.com
            carol: carol@btca.com
            alice: alice@btca.com
    ''').strip()
    assert result1 == expected1
    assert result2 == expected1
    result3 = '{:{{v.name}}={{v.email}}}'.format(C)
    expected3 = 'bob=bob@btca.com ted=ted@btca.com carol=carol@btca.com alice=alice@btca.com'
    assert result3 == expected3
