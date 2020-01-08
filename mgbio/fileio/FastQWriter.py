#!/usr/bin/python

"""
FastQWriter.py

Writer for FASTQ Files

Author : Thomas Sunghoon Heo
"""

class FastQWriter:
    def __init__(self, fname, gzip=False):
        if gzip:
            self.out = gzip.open(fname, "wb")
        else:
            self.out = open(fname , "w")
    def write_line(self, line):
        if line[-1] == '\n':
            self.out.write(line)
        else:
            lline = line + '\n'
            self.out.write(lline)
    def write_block(self, name, seq, qual, comment = None):
        if comment != None:
            _name = name + ' ' + comment + '\n'
        _seq = seq.rstrip() + '\n'
        _qual = qual.rstrip() + '\n'
        if len(_seq) != len(_qual):
            raise Exception("Sequence and QualityStrings do not match")
        self.write_line(_name)
        self.write_line(_seq)
        self.write_line(_qual)


