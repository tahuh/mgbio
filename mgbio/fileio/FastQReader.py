#!/usr/bin/python

"""
FastQReader.py

Originally in SequenceParser.py of my github repository https://github.com/tahuh/SynbioBioModule/blob/master/SequenceParser.py

Author : Thomas Sunghoon Heo
"""

from mgbio.fileio.gzip_checker import gzip_check

class FastQReader:
    def __init__(self, fname=None):
        self.fname = fname
        self.fobj = None
    def open(self, fname=None):
        if self.fname == None:
            if fname == None:
                raise IOError("Cannot open NONE file")
            else:
                self.fname = fname
        self.fobj = gzip_check(self.fname)
    def rewind(self):
        self.fobj.seek(0)
    def close(self):
        self.fobj.close()
    def next(self):
        l1 = self.fobj.readline()
        id = l1.split()[0][1:]
        try:
            desc = l1.rstrip().split()[1]
        except:
            desc = ''
        seq = self.fobj.readline().rstrip()
        self.fobj.readline()
        qual = self.fobj.readline().rstrip()
        return id, desc, seq, qual
    def parse(self):
        id = ''
        desc = ''
        seq = ''
        qual = ''
        for i, line in enumerate(self.fobj):
            if i % 4 == 0 :
                id = line.rstrip().split()[0][1:]
                try:
                    desc = line.rstrip().split()[1]
                except:
                    desc = ''
            elif i% 4 == 1:
                seq = line.rstrip()
            elif i% 4 == 2:
                continue
            else:
                qual = line.rstrip()
                yield id, desc, seq, qual
