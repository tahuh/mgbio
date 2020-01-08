#!/usr/bin/python

"""
DNA.py

class that defines DNA string

Author : Thomas Sunghoon Heo
"""

NUCLEOTIDES_COMP_DICT = { 'A' : 'T' , 'G' : 'C' , 'C' : 'G' , 'T' : 'A' , 'N' : 'N'}
class DNA:
    def __init__(self, seq=None):
        self.seq = seq
        if(self.seq != None):
            self.seq = sefl.seq.upper()
    def __len__(self):
        if self.seq != None:
            return len(self.seq)
        else:
            return -1
    def __hash__(self):
        return hash(self.seq)
    def __eq__(self, other):
        return self.seq == other.seq
    def __ne__(self, other):
        return self.seq != other.seq
    def __invert__(self):
        # Create complement using bit operation
        tmp = [ NUCLEOTIDES_COMP_DICT[b] for b in self.seq]
        return DNA(seq = "".join(tmp))
    def __add__(self, other):
        if(other.seq == None):
            raise Exception()
        self.seq = self.seq + other.seq
    def __getitem__(self, item):
        if isinstance(item, tuple):
            return [self.seq[i] for i in item]
        elif isinstance(item, slice):
            return self.seq[item]
        else:
            return self.seq[item]
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            if len(key) != len(value):
                raise Exception()
            s_list = list(self.seq)
            for i, k in enumerate(key):
                s_list[k] = value[i]
            self.seq = "".join(s_list)
        elif isinstance(key, slice):
            s_list = list(self.seq)
            for i, j in enumerate(range(key.stop, key,end, key.step)):
                s_list[j] = value[i]
            self.seq = "".join(s_list)
        else:
            s_list = list(self.seq)
            s_list[key] = value
            self.seq = "".join(s_list)
    def seq(self):
        return self.seq
    def set_seq(self, seq):
        self.seq = seq
    def complement(self):
        tmp = [NUCLEOTIDES_COMP_DICT[b] for b in self.seq]
        return DNA(seq = "".join(tmp))
    def complement_inplace(self):
        tmp = self.complement()
        self.seq = tmp.seq
    def reverse_complement(self):
        comp = self.complement()
        comp.seq = comp.seq[::-1]
        return comp
    def reverse_complement_inplace(self):
        tmp = self.reverse_complement()
        self.seq= tmp.seq
