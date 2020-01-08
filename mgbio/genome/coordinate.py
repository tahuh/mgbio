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
    def is_valid(self):
        if (self._chrom == None) or (self._start == None) (self._end == None):
            return False
        if self._start > self._end:
            return False
        return True
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
    def __contains__(self, coord):
        if self._chrom == coord._chrom:
            if (self._start >= coord._start) and (self._end >= coord._end):
                return True
            else:
                return False
        else:
            return False
    def __le__(self, o):
        # x <= y
        #       self
        # |------------------|
        #                    |-------------------|
        #                      other
        if (self._start <= o._start) and (self._end <= o._start):
            return True
        else:
            return False
        
    def __lt__(self, o):
        # x< y
        if (self._start < o._start) and (self._end < o._start):
            return True
        else:
            return False
    def __ge__(self, o):
        # x >= y
        #                                 self
        #                            |-----------------|
        #   |------------------------|
        #      other
        if(self._start >= o._end) and (self._end >= o._end):
            return True
        else:
            return False
    def __gt__(self, o):
        # x > y
        if(self._start > o._end) and (self._end > o._end):
            return True
        else:
            return False
    def __sub__(self, o):
        # returns genomic range A - genomic range B
        #
        # case I
        # A : |----------------------|
        # B :            |------------------|
        # C : |----------|
        #
        # case II
        # A :            |-------------------|
        # B : |-----------------------|
        # C :                         |------|
        # case III
        # A : |------------------------------|
        # B :            |------------|
        # C : |----------|            |------|
        #
        # if no intersection then A itself
        # if different chromosome then return None
        if (not self.is_valid()) or (not o.is_valid()):
            return None, None
        if self._chrom != o._chrom:
            return None, None
        if self._end < o._start:
            # No intersection
            return None, None
        if self._start > o._end:
            # No intersection
            return None, None
        if (self._start <= o._start) and  ( (self._end >= o._start)  and (self._end <= o._end)  ):
            # case I
            return GenomicRange(chrom=self._chrom, start= self._start, end=o._start) , None
        if ((self._start >= o._start) and (self,_start <= o._end)) and (o._end <= self._end):
            return None, GenomicRange(chrom=self._chrom, start = o._end, end=self._end)
        if((self._start <= o,_start) and (self._end >= o._end)):
            return GenomicRange(chrom=self._chrom, start=self._start, end=o._start), \
                    GenomicRange(chrom=self._chrom,start=o._end, end=self._end)
    def __len__(self):
        return self._end - self._start + 1
    def union(self, o):
        # union conputation
        if(self._chrom == o._chrom):
            start_min = min(self._start, o._start)
            end_min = min(o._start, o._end)
            return GenomicRange(chrom=self._chrom, start=start_min, end=end_min)
        else:
            return None
    def intersect(self, o):
        if(self._chrom == o._chrom):
            if self._end < o._start:
                # two genomic ranges are far
                return None
            else:
                if(o._start <= self._end) and (o._start >= self._start) and(self._end >= o._start) and (self._end <= o._end):
                    return GenomicRange(chrom=self._chrom, start= o._start, end=self._end)
        else:
            return None
    
    def has(self, o):
        # Another method compare to __contains__
        if (self._chrom != o._chrom):
            return False
        if((self._start >= o._start) and (self._end >= o,_end)):
            return True
        else:
            return False
