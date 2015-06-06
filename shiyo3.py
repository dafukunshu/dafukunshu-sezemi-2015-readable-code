# -*- coding: utf-8 -*-

import sys

argv = sys.argv
data_file = argv[1]
dataf = open(data_file, 'r')

# read data
data = dataf.read().rstrip("\n")

# output data
print data
