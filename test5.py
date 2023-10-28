heights = [1, 2, 6, 3]
# heights = [2, 10, 5, 3, 2]
# [1, 2, *3*, 6, 3, *2*]


def get_result(heights):
	count = len(heights)
	heights = [1] + heights + [1]
	arr = []
	for idx, height in enumerate(heights):
		if idx == len(heights) - 1:
			break
		little = min(heights[idx], heights[idx+1])
		big = max(heights[idx], heights[idx+1])
		more = big / little
		if more > 2:
			while little < big:
				little *= 2
				if little >= big:
					break
				count += 1

	return count

print(get_result(heights))