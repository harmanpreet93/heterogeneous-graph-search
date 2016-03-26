#!/usr/bin/python
import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Usage: tsv2csv.py input.tsv output.csv")

print "Please wait, this may take few seconds..."
csv.field_size_limit(sys.maxsize)
csv.writer(file(sys.argv[2], 'w+')).writerows(csv.reader(open(sys.argv[1]), delimiter="\t"))
