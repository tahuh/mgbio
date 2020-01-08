#!/usr/bin/python

"""
coordinate.py

Genomic coordinates

Author : Thomas Sunghoon Heo
"""

class GenomicCoordinate:
    def __init__(self, chrom=None, pos=None):
        self._chrom=chrom
        if pos != None:
            self._pos = int(pos)
        else:
            self._pos=pos
    def chrom(self):
        return self._chrom
    def pos(self):
        return self._pos
    def set_chrom(self, c):
        self._chrom = c
    def set_pos(self, p):
        self._pos = int(p)
    def __eq__(self, other):
        return (self._chrom == other._chrom) and (self._pos == other._pos)
    def __ne__(self, other):
        return (self._chrom != other._chrom) or (self._pos != other._pos)
    def __hash__(self):
        key_str = self._chrom + '_' + str(self._pos) # this is always unique
        return hash(key_str)

class GenomicRange:
    def __init__(self, chrom=None, start=None, end=None):
        self._chrom = chrom
        self._start = start
        self._end = end
        if(start != None):
            self._start = int(start)
        if end != None:
            self._end = int(end)
    def chrom(self):
        return self._chrom
    def start(self):
        return self._start
    def end(self):
        return self._end
    def set_chrom(self, c):
        self._chrom = c
    def set_start(self, s):
        self._start = int(s)
    def set_end(self, e):
        self._end = int(e)
    def __eq__(self, o):
        return ((self._chrom == o._chrom) and (self._start == o._start) and (self._end == o.end))
    def __ne__(self, o):
        return ((self._chrom != o._chrom) or (self._start != o._start) or (self._end != o.end))
    def __hash__(self):
        key_str = self._chrom + '_' + str(self._start) + '_'+ str(self._end)
        return hash(key_str)
