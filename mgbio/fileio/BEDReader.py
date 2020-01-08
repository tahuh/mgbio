#!/usr/bin/python

"""
BEDReader.py

Reader class for BED file

Author : Thomas Sunghoon Heo
"""

class BEDReader:
    # Usually BED files are not that much large
    # So we directly parse all BED records into pandas-like data frame
    # Then access via column names to retrieve data or row index
    def __init__(self, fname, fmt="BED3", header=None, rownames=None):
        self.fobj = open(fname)
        default_header = ["chrom", "start", "end"]
        self.rows = []
        self.cols = []
        ncols = 0
        for i, line in enumerate(self.fobj):
            data = line.rstrip().split("\t")
            if i == 0 :
                ncols = len(data)
            if ncols != len(data):
                raise Exception("At BED file line %d, number of columns are different by others"%(i))
            self.rows.append(data)
        self.fobj.seek(0)
        # Setup header
        if header != None:
            if len(header) == ncols:
                self.header = header
            else:
                extra = ncols - 3
                for i in range(extra):
                    default_header.append("extra" + str(i+1))
                self.header = default_header
        self.hdr2idx = {}
        for i, h in enumerate(self.header):
            self.hdr2idx[h] = i
        # Now we make column data
        for cid in range(ncols):
            tmp = []
            for rid in len(self.rows):
                tmp.append(self.rows[rid][cid])
            self.cols.append(tmp)
        # Setup rownames
        self.rownames = rownames
        if self.rownames == None:
            self.rownames = []
            for i in range(self.rows):
                self.rownames.append("row" + str(i+1))
        self.row2idx = { r : i for (i,r) in enumerate(self.rownames)}
    def nrows(self):
        return len(self.rows)
    def ncols(self):
        return len(self.cols)
    def row_names(self):
        return self.rownames
    def col_names(self):
        return self.header
    def access_row_by_rowname(self, rowname):
        idx = self.row2idx[rowname]
        return self.rows[idx]
    def access_row_by_index(self, rid):
        return self.rows[rid]
    def access_col_by_colname(self, colname):
        idx = self.hdr2idx[colname]
        return self.cols[idx]
    def access_col_by_index(self, cid):
        return self.cols[cid]
