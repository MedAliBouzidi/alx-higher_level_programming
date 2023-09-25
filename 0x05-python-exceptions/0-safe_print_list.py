#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	for idx in range(x1):
		try:
			printi("{}".format(my_list[idx]), end='')
		except IndexError:
			break
	print("")
	return idx
