#!/usr/bin/python

"""
allele.py

Allele defines

Author : Thomas Sunghoon Heo
"""
from mgbio.genome import GenomicCoordinate
from mgbio.sequence.DNA import DNA

class Allele(GenomicCoordinate):
    def __init__(self,chrom=None,pos=None,base=None):
        super().__init__(chrom=chrom,pos=pos)
        self._allele = base
        if self._allele != None:
            if isinstance(self._allele, str):
                self._allele = DNA(seq=base)
    def __eq__(self, o):
        v1 = super().__eq__(o)
        # sincle _allele is DNA class we have defined eq
        v2 = (self._allele == (o._allele))
        return (v1 == True and v2 == True)
    def __ne__(self, o):
        v1 = super().__ne__(o)
        v2 = (self._allele != o._allele)
        return ((v1 == True) or (v2==True))
    def __hash__(self):
        s = self._allele.seq
        key_str = self._chrom + '_'+str(self._pos) + '_' + s
        return hash(key_str)
    def allele(self):
        return self._allele
    def set_allele(self, allele):
        if isinstance(allele , DNA):
            self._allele = allele
        else:
            self._allele = DNA(seq=allele)
