#! /usr/bin/env python

import sys
import pdb
import re

filename = sys.argv[1]
results_folder = sys.argv[2]

out = open(results_folder + "/luo-2012-supp-table-5-formatted.txt",mode = 'w')

for line in open(filename):

    
    lines = line.split("\r")

    for line in lines:
        if line.startswith("Sample"):
            continue

        else:
            
            line = re.sub('"','', line)

            fields = line.strip().split(",")
            chrom = fields[1]
            start = fields[2]
            end = fields[3]
            down_genes = fields[6].split(",")
            up_genes = fields[7].split(",")
            down_nearbys = fields[8].split(",")
            up_nearbys = fields[9].split(",")



            if len(down_genes) == 1:

                gene = down_genes[0]
            
                toprint = [chrom, start, end, gene]
                print >> out, "\t".join(toprint)
        
            else:
                for gene in down_genes:
                

                    toprint = [chrom, start, end, gene]
                    print >> out, "\t".join(toprint)
            

            if len(up_genes) == 1:

                gene = up_genes[0]
            
                toprint = [chrom, start, end, gene]
                print >> out, "\t".join(toprint)
            else:
                for gene in up_genes:
                

                    toprint = [chrom, start, end, gene]
                    print >> out, "\t".join(toprint)
        
            if len(down_nearbys) == 1:

                gene = down_nearbys[0]
            
                toprint = [chrom, start, end, gene]
                print >> out, "\t".join(toprint)
            else:
                for gene in down_nearbys:
                

                    toprint = [chrom, start, end, gene]
                    print >> out, "\t".join(toprint)


            if len(up_nearbys) == 1:

                gene = up_nearbys[0]
            
                toprint = [chrom, start, end, gene]
                print >> out, "\t".join(toprint)
            else:
                for gene in up_nearbys:
                

                    toprint = [chrom, start, end, gene]
                    print >> out, "\t".join(toprint)
