import sys

treeStr = sys.argv[1]

from math import floor,ceil,log

def levelCount(treeStr):
	# Write code here
	ls = treeStr.split()
	n = len(ls)
	return ceil(log(n+1,2))

print(levelCount(treeStr))
