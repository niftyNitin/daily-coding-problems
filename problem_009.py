def max_alt_sum(nums):
	incl_sum = 0
	excl_sum = 0
	for num in nums:
		t = max(incl_sum, excl_sum)
		incl_sum = excl_sum + num
		excl_sum = t

	return max(incl_sum, excl_sum)


print(max_alt_sum([5,5,10,40,50,35]))
