#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	if isinstance(my_list, list):
		try:
			for idx in range(x + 1):
				print(my_list[idx], end='')
		except:
			pass
		print(end="\n")
		return idx
