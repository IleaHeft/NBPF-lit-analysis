#! /usr/bin/env python

import sys
import pdb

filename = sys.argv[1]
results_folder = sys.argv[2]

out = open(results_folder + "/glatt-2012-diff-expressed-probes-formatted.csv", mode = 'w') 

print >> out, "Probe.ID", ",","Gene.Symbol"

for line in open(filename):

    lines = line.split("\r")


    for line in lines:
        if line.startswith("ILMN_"):
            fields = line.strip().split(" ")
            probeID = fields[0]
            gene = fields[1]

            toprint = [probeID, gene]

            print >> out, ",".join(toprint)

        else:
            continue
