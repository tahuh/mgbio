#!/usr/bin/python

import random
out = open("test.ref.fasta", "w")
for i, length in enumerate([1000, 2000, 3000]):
    seq = [random.choice("ATGC") for _ in range(length)]
    out.write('>ref' + str(i) + ' ' + 'comment' + str(i) + '\n' + "".join(seq) + '\n')

