
import math

from common import get_data, get_toys_dict

def _iter_possible(lst_final, num_missing_parts, num_packed_gifts, lst_all_possible, given=None):
	
	#================================#
	# 1st run = no "given" values (start with no assumptions)
	if given is None:
		given = []
	#================================#
	
	#================================#
	# count up total USED given "given"
	parts_already_used = 0
	
	for idx, toy_tup in enumerate(lst_final):
		
		try:
			g = given[idx]
		except IndexError:
			break
		
		toy_name, num_parts = toy_tup
		
		parts_already_used += (num_parts * g)
	
	parts_remaining = num_missing_parts - parts_already_used
	#================================#
	
	#================================#
	# index of "current" row being tried
	current_row = len(given)
	
	# iterate backward so larger values tried first
	for possible_val in lst_all_possible[current_row][::-1]:
		
		toy_parts = lst_final[current_row][1]
		
		possible_parts = possible_val * toy_parts
		
		possible_remainder = parts_remaining - possible_parts
		
		# in all cases: if Remainder == 0, CHECK if solution is found
		if possible_remainder == 0:
			
			final_val = [x for x in given] + [possible_val]
			
			if sum(final_val) == num_packed_gifts:
				
				yield final_val
				
			else:
				
				# solution is INVALID -- all parts accounted for BUT wrong number of gifts
				pass
		
		elif possible_remainder < 0:
			
			# solution is INVALID -- not enough parts left for this scenario
			pass
		
		else:
			
			# there are some parts left over:
			
			# if this is the LAST row
			if current_row == len(lst_all_possible) - 1:
				
				# solution is INVALID -- no more rows to try
				pass
			
			else:
				
				# not the last row, so keep going
				
				next_given = [x for x in given] + [possible_val]
				
				# pre-eliminate if not possible
				# - ("greater than" check here because _might_ be == with remaining rows all 0!)
				
				if sum(next_given) > num_packed_gifts:
					
					# solution is INVALID -- too many gifts
					pass
				
				else:
					
					yield from _iter_possible(lst_final, num_missing_parts, num_packed_gifts, lst_all_possible, given=next_given)
	
	#================================#
	
	return


if __name__ == "__main__":
	
	#================================#
	# this number is a constant provided by "part2_en.md"
	num_packed_gifts = 20
	
	# HARDCODED list of things that are 'parts'
	names_parts = (
		'Printplaat', 
		'Accu', 
		'Schokdemper', 
		'Batterij', 
		'BatmobileChassis', 
		'AutoChassis', 
		'Wiel', 
		'Unobtanium', 
	)
	#================================#
	
	#================================#
	# get part counts (same behavior as in Part 1)
	
	num_missing_parts, toy_rows = get_data()
	
	d_toys = get_toys_dict(toy_rows)
	#================================#
	
	#================================#
	# filter by things that are toys
	
	lst_toys_only = []
	
	for toy_name, toy_info in d_toys.items():
		
		if toy_name in names_parts:
			continue
		
		lst_toys_only.append((toy_name, toy_info['num']))
	
	# sort so "bigger" toys will be tried first (optional)
	lst_toys_only.sort(key=lambda x: x[1], reverse=True)
	#================================#
	
	#================================#
	# narrow down range of possibile quantities for each toy
	
	lst_all_possible = []
	
	for idx, toy_tup in enumerate(lst_toys_only):
		
		toy_name, num_toy_parts = toy_tup
		
		max_count = math.floor(num_missing_parts / num_toy_parts)
		
		# limit by maximum # of gifts packed
		if max_count > num_packed_gifts:
			max_count = num_packed_gifts
		
		lst_row_possible = []
		for x in range(max_count + 1):
			lst_row_possible.append(x)
		
		lst_all_possible.append(lst_row_possible)
	#================================#
	
	#================================#
	# iterate over all possibilities
	
	solutions = [x for x in _iter_possible(lst_toys_only, num_missing_parts, num_packed_gifts, lst_all_possible)]
	
	# NOTE: got _all_ solutions so can ensure that EXACTLY 1 is valid
	assert len(solutions) == 1
	#================================#
	
	#================================#
	# get final answer
	
	lst_final_str = []
	
	for idx, num_quant in enumerate(solutions[0]):
		
		toy_name = lst_toys_only[idx][0]
		
		for x in range(num_quant):
			
			lst_final_str.append(toy_name[0])
	
	# sort by alpha
	lst_final_str.sort()
	
	str_final = ''.join(lst_final_str)
	#================================#
	
	print(str_final)
	
