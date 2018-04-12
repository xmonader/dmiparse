"""dmiparse - Parse dmidecode into reasonable python"""

__version__ = '0.1.0'
__author__ = 'Ahmed Youssef <xmonader@gmail.com>'
__all__ = ['dmiparse']


import json
from itertools import takewhile

MODE_SECTION_START, MODE_SECTION_NAME, MODE_READ_KV, MODE_LIST_PROPERTY, MODE_SECTION_DONE = range(5)

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
    mode = None
    sects = {} # title => section 
    getindentlevel = lambda l:  len(list(takewhile(lambda c: c.isspace(), l)))
    s = None
    p = None
    for i, l in enumerate(lines):
        if l.startswith("Handle"):
            mode = MODE_SECTION_START
            s = Section()
            s.handleline = l
            mode = MODE_SECTION_NAME
            continue 

        if l == "": # can be just new line before reading any sections. 
            if s is not None:
                sects[s.title] = s
            continue

        if mode == MODE_SECTION_NAME:
            s.title = l
            mode = MODE_READ_KV
        elif mode == MODE_READ_KV:
            k, v = [x.strip() for x in l.split(":")]
            p = Property(v)
            if i < len(lines) and getindentlevel(l) < getindentlevel(lines[i+1]):
                mode = MODE_LIST_PROPERTY
            else:
                s.props[k] = p
        elif mode == MODE_LIST_PROPERTY:
            p.add_item(l.strip())
            if getindentlevel(l) > getindentlevel(lines[i+1]):
                mode = MODE_READ_KV
                s.props[k] = p

    return sects

