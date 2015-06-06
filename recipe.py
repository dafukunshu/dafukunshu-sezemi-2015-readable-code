# -*- coding: utf-8 -*-

import sys

argv = sys.argv
data_file = argv[1]

# read data
dataf = open(data_file, 'r')
recipes = dataf.read().splitlines()
recipe_num = len(recipes)

# output data
i = 0
while i < recipe_num:
  print recipes[i]
  i += 1

