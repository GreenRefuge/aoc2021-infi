
import re

#================================#
def get_data():
	
	with open('4IW9MA8JLE7W', 'r') as f:
		data = f.read()
	
	rows = [x for x in data.split('\n') if x != '']
	
	# !! assumes match
	num_missing_parts = int(re.match(r'^(\d+) .*$', rows[0]).groups()[0])
	toy_rows = rows[1:]
	
	return (num_missing_parts, toy_rows)
#================================#

#================================#
def _get_parts_count_for_toy(d_toys, toy_name):
	
	t_info = d_toys[toy_name]
	
	count_parts = 0
	
	for part_name, part_count in t_info['parts'].items():
		
		if part_name in d_toys:
			# recursively get # of parts
			num_parts = part_count * _get_parts_count_for_toy(d_toys, part_name)
		else:
			num_parts = part_count * 1
		
		count_parts += num_parts
	
	return count_parts
#================================#

#================================#
def get_toys_dict(toy_rows):
	
	d_toys = {}
	
	#================================#
	# 1st pass - get part names/quants for each toy
	
	for row in toy_rows:
		
		# !! assumes valid input
		m = re.match(r'^(.*?): (.*)$', row)
		
		toy_name, str_parts = m.groups()
		
		lst_str_parts = str_parts.split(',')
		
		d_parts = {}
		
		for str_part in lst_str_parts:
			
			str_strip = str_part.strip()
			
			m = re.match(r'^(\d+) (.*)$', str_strip)
			
			part_quant_str, part_name = m.groups()
			
			d_parts[part_name] = int(part_quant_str)
		
		d_toys[toy_name] = {
			'parts': d_parts, 
			# placeholder
			#'num': None, 
		}
	#================================#
	
	#================================#
	# 2nd pass - get total parts count for each toy
	
	for toy_name, t_info in d_toys.items():
		
		t_info['num'] = _get_parts_count_for_toy(d_toys, toy_name)
	#================================#
	
	return d_toys
#================================#
