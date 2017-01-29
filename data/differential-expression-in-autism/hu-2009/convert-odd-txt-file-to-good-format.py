#! /usr/bin/env python

import sys
import pdb
import re


filename = sys.argv[1]
name_for_new_file = sys.argv[2]
result_folder = sys.argv[3]

list_of_genes = []

out = open(result_folder + "/" + name_for_new_file, mode = 'w')

for line in open(filename):
    
    line = re.sub("\r+","\n", line)
    line = re.split("\n+", line)
    #line = re.split("\n+", line)


    for item in line:
        if "." not in item:
            list_of_genes.append(item)



    print >> out, "GENE_SYMBOL"

for gene in list_of_genes:
    
    gene = gene.strip()
    gene = re.sub(" ","", gene)

    if "#" in gene or "SYMBOL" in gene or "GENE" in gene:
        continue
    else:
        print >> out, gene
