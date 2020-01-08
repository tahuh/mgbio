#!/usr/bin/python

"""
gzip_checker.py

Originally format_checker in https://github.com/tahuh/SynbioBioModule/blob/master/SequenceParser.py

Author : Thomas Sunghoon Heo
"""

import gzip

def gzip_check(fname):
    fobj = open(fname, "rb")
    byts = fobj.read(3)
    if byts == "\x1f\x8b\x08": # gzip magic string
        fobj.seek(0)
        return gzip.GzipFile(fname, fileobj=fobj)
    else:
        fobj.seek(0)
        return fobj
