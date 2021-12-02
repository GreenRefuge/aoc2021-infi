
from common import get_data, get_toys_dict

if __name__ == "__main__":
	
	num_missing_parts, toy_rows = get_data()
	
	d_toys = get_toys_dict(toy_rows)
	
	# sort by total# of parts (most first)
	lst_final = sorted([(k, v['num']) for k, v in d_toys.items()], key=lambda x: x[1], reverse=True)
	
	print(lst_final[0][1])
	
