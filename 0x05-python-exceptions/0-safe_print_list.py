#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	for idx in range(x + 1):
		try:
			printi("{}".format(my_list[idx]), end='')
		except:
			break
	print("")
	return idx
