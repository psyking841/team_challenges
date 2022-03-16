from collections import defaultdict

def func1(n):
	for i in range(1, n+1):
		if i % 3 == 0 and i % 5 == 0:
			print("FuzzBuzz")
		elif i % 3 == 0:
			print("Fuzz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

def func2(strs):
	map = defaultdict(list)
	for s in strs:
		map[tuple(sorted(s))].append(s)
	return list(map.values())