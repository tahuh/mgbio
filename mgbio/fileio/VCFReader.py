#!/usr/bin/python

"""
VCFReader.py

Utility to read VCF file

Author : Thomas Sunghoon Heo
"""

from mgbio.fileio.gzip_checker import gzip_check

class VCFRecord:
    def __init__(self, vcf_line, sample_names= None):
        self.init(vcf_line, sample_names=sample_names)
    def get_all_aux(self, aux_key):
        return self.fmt_dict[fmt_key]
    def get_sample_aux(self, aux, sample_name):
        a = self.fmt_dict[aux]
        return a[self.sample_name_dict[sample_name]]
    def get_info(self, info_key):
        return self.info_dict[info_key]
    def init(self, vcf_line, sample_names=None):
        data = vcf_lines.rstrip().split("\t")
        if len(data) < 8:
            raise Exception("Required VCF mandatory fields are missing %s"%(vcf_line))
        # Mandatory fields
        self.chrom = data[0]
        self.pos = data[1]
        self.id = data[2]
        self.ref = data[3]
        self.alt = data[4]
        self.qual = data[5]
        self.filter = data[6]
        self.info = data[7]
        self.info_dict = {}
        for kv in self.info.split(";"):
            if '=' in kv:
                kvv = kv.split('=')[0]
                k = kvv[0]
                v = kvv[1]
                self.info_dict[k] = v
            else:
                self.info_dict[kv] = None
        self.fmt = None
        self.sample_names=None
        self.sample_name_dict = {}
        self.fmt_array = []
        self.fmt_dict = {}
        if len(data) >= 10 :
            self.sample_names = sample_names
            others = data[9:]
            if (self.sample_names != None) and (len(self.sample_names) != len(others)):
                raise Exception("Malformed VCF record. Specified number of samples in VCF file is differ from the records")
            if (self.sample_names == None):
                self.sample_names = []
                for i in range(1,len(others) + 1):
                    self.sample_names.append("sample%d"%(i))
            for i, name in self.sample_names:
                self.sample_name_dict[name] = i # array index
            self.fmt = data[8].split(':')
            for elem in data[9:]:
                self.fmt_array.append(elem.split(':'))
            for kidx, k in enumerate(self.fmt):
                for value in self.fmt_array:
                    try:
                        self.fmt_dict[k].append(value[kidx])
                    except KeyError:
                        self.fmt_dict[k] = [value[kidx]]
