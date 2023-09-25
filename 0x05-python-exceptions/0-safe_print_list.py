#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	if isinstance(my_list, list):
		for idx in range(x + 1):
			try:
				print(my_list[idx], end='')
			except:
				break
		print("")
		return idx
