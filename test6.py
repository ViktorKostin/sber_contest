import itertools
fences = [1,2,3]

def through_fences(fences_2):
	current_fence = fences_2[0]
	i = 1
	if current_fence < 0 or sum(fences_2) < 0:
		return False
	while i <= len(fences_2):
		try:
			current_fence = fences_2[current_fence] + current_fence
			if current_fence+1 == len(fences_2):
				return True
			i+=1
		except:
			return False
	return False

def get_result(fences):
	if sum(fences) < 0:
		return False
	for fence in itertools.permutations(fences):
		result = through_fences(fence)
		if result:
			print(fence)
	return False
	

print(get_result(fences))