array_steps = ["d", "d", "d", "u", "u", "d", "u"]

def get_result(array_steps):
	depth_array = []
	count = 0
	depth_array.append(0)
	for step in array_steps	:
		if step == "d":
			count-=1
		if step == "u":
			count+=1
		depth_array.append(count)
	max_depth = -min(depth_array)
	min_depth = max(depth_array)

	return max_depth

get_result(array_steps)