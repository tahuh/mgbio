#!/usr/bin/python

"""
Kmer.py

Defines k-mer

Author : Thomas Sunghoon Heo
"""

from mgbio.sequence.DNA import DNA

class Kmer(DNA):
    def __init__(self, seq=None, weight=0.0):
        super().__init__(seq=seq)
        self.weight=weight
    def set_weight(self, w):
        self.weight = w
    def get_weight(self):
        return self.weight
    def update_weight(self, w):
        self.weight = self.weight + w
    def generate_right_kmers(self):
        kms = []
        for base in ['A' , 'T', 'G' , 'C']:
            km = Kmer(seq = self.seq[1:] + base)
            kms.append(km)
        return kms
    def generate_left_kmers(self):
        kms = []
        for base in ['A', 'T', 'G', 'C']:
            km = Kmer(seq = base + self.seq[:-1])
            kms.append(km)
        return kms
    def is_left_of(self, km):
        seq1 = self.seq
        seq2 = km.seq
        if seq1[1:] == seq2[:-1]:
            return True
        else:
            return False
    def is_right_of(self, km):
        seq1 = self.seq
        seq2 = km.seq
        if seq1[:-1] == seq2[1:]:
            return True
        else:
            return False


