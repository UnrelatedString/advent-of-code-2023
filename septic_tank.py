from typing import List
from collections.abc import Iterable

import string
import itertools as itr
import more_itertools as mitr
from collections import defaultdict, deque
from functools import lru_cache

alpha = string.ascii_lowercase

def slorp():
    return [line.strip('\n') for line in open(0)]

def line_groups(lines) -> List[List[str]]:
    return [group.split('\n') for group in '\n'.join(lines).strip('\n').split('\n\n')]

'''
Recursively split on a series of delimiters
'''
def serial_split(string: str, delimiters):
    if delimiters:
        head, *tail = delimiters
        return (serial_split(slice, tail) for slice in string.split(head))
    else:
        return string

moore = 1,1+1j,1j,-1+1j,-1,-1-1j,-1j,1-1j
von_neumann = 1,1j,-1,-1j

def c_t(z):
    return z.real, z.imag

def bidict(d):
    ret = {k:set() for k in itr.chain(d.keys(),d.values())}
    for k,v in d.items():
        ret[k].add(v)
        ret[v].add(k)
    return ret

def windows(l,n):
    return [l[i:i+n] for i in range(len(l)-n+1)]

def zind(z,g):
    return g[int(z.imag)][int(z.real)]

def zround(z):
    return complex(round(z.real), round(z.imag))

def rotate(m):
    return list(zip(*m))[::-1]

def inclusive(a, b):
    if a > b:
        a, b = b, a
    return range(int(a), int(b+1))

def tuple_augment(into, at, f):
    return (*into[:at], f(into[at]), *into[at+1:])
