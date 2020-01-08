#!/usr/bin/python

"""
FastAReader.py

Originally in SequenceParser.py of my github repository https://github.com/tahuh/SynbioBioModule/blob/master/SequenceParser.py

Author : Thomas Sunghoon Heo
"""

from mgbio.fileio.gzip_checker import gzip_check

class FastAReader:
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
    def parse(self):
        id = ''
        desc = ''
        seq_trail = []
        for line in enumerate(self.fobj):
            if line.startswith('>'):
                if seq_trail:
                    yield id , desc, "".join(seq_trail)
                id = line.rstrip().split()[0][1:]
                try:
                    desc = line.rstrip().split()[1]
                except:
                    desc = ''
                seq_trail = []
            else:
                seq_trail.append(line.rstrip())
        if seq_trail:
            yield id, desc, "".join(seq_trail)
