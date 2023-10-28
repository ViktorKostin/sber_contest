import itertools
import random
fences = [0, 2, 1, 7, 0, -1, -4, 0]

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
			if current_fence+1 > len(fences_2):
				return False
			i+=1
		except:
			return False
	return False

def get_result(fences):
	for i in range(100):
		random.shuffle(fences)
		result = through_fences(fences)
		if result:
			print(fences)
	return False
	

print(get_result(fences))