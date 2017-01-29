#! /usr/bin/env python

import sys
import pdb
import re

filename = sys.argv[1]
output = sys.argv[2]

out = open(output, mode = 'w')

for line in open(filename):

    lines = line.split("\r")
    
    for line in lines:
        fields = line.strip().split(",")
        genes = fields[6]

        if "///" in genes:
            genes = genes.split("///")

            for gene in genes:
                
                gene = re.sub(" ","",gene)
                print >> out, gene

        else:
            print >> out, genes
