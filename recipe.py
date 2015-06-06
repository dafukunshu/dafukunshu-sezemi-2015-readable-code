# -*- coding: utf-8 -*-

import sys

def print_all_recipe(recipes):
  recipe_num = len(recipes)
  i = 0
  while i < recipe_num:
    print "%d: %s" % (i+1, recipes[i])
    i += 1

def print_selected_recipe(recipes, id):
  print "%d: %s" % (recipe_id, recipes[recipe_id - 1])

argv = sys.argv
argv_len = len(argv)
if argv_len <= 2:
  print "Usage: python %s recipe-data recipe_id"
  quit()

recipe_fname = argv[1]
recipe_id = int(argv[2])

# read data
recipef = open(recipe_fname, 'r')
recipes = recipef.read().splitlines()

# output data
# print "%d: %s" % (recipe_id, recipes[recipe_id - 1])
# print_all_recipe(recipes)
print_selected_recipe(recipes, id)
