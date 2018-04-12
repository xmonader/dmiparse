"""dmiparse - Parse dmidecode into reasonable python"""

__version__ = '0.1.0'
__author__ = 'Ahmed Youssef <xmonader@gmail.com>'
__all__ = ['dmiparse']


import json
from itertools import takewhile

STATE_SECTION_NAME, STATE_READ_KV, STATE_LIST_PROPERTY = range(3)

class Section:
    def __init__(self):
        self.props = {}
        self.title = ""
        self.handleline = ""

    def __str__(self):
        return str(self.__dict__)

class Property:
    def __init__(self, val):
        self.val = val
        self.items = []
    
    def add_item(self, i):
        self.items.append(i)

    def __str__(self):
        return str(self.__dict__)


def dmiparse(s):
    """Parses dmidecode output into json
    
    Arguments:
        s {string} -- dmidecode output. 
    
    Returns:
        dict -- section name => section object
    """

    lines = s.splitlines()
    state = None
    sects = {} # title => section 
    getindentlevel = lambda l:  len(list(takewhile(lambda c: c.isspace(), l)))
    s = None
    p = None
    for i, l in enumerate(lines):
        if l.startswith("Handle"):
            s = Section()
            s.handleline = l
            state = STATE_SECTION_NAME
            continue 

        if l == "": # can be just new line before reading any sections. 
            if s is not None:
                sects[s.title] = s
            continue

        if state == STATE_SECTION_NAME:
            s.title = l
            state = STATE_READ_KV
        elif state == STATE_READ_KV:
            k, v = [x.strip() for x in l.split(":")]
            p = Property(v)
            if i < len(lines) and getindentlevel(l) < getindentlevel(lines[i+1]):
                state = STATE_LIST_PROPERTY
            else:
                s.props[k] = p
        elif state == STATE_LIST_PROPERTY:
            p.add_item(l.strip())
            if getindentlevel(l) > getindentlevel(lines[i+1]):
                state = STATE_READ_KV
                s.props[k] = p

    return sects

