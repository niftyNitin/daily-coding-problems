def count_ways(n, x):
	if n == 0:
		return 1
	nums = [0] * (n+1)
	nums[0] = 1
	for i in range(1, n+1):
		total = 0
		for j in x:
			if (i-j) >= 0:
				total += nums[i-j]
		nums[i] = total

	return nums[n]

n = 4
x = [1, 2]
print(count_ways(n, x))