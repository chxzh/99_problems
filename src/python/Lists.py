# find the last
# Find the last element of a list
# example input/output:
# in: [1,2,3,4]
# out: 4
def find_the_last(lst):
	return lst[-1] 

# find the last but one
# Find the last but one element of a list
# example input/output:
# in: [1,2,3,4]
# out: 3
def find_the_last_but_one(lst):
	return lst[-2]
	
# find the kth
# Find the Kth element of a list. The first element in the list is number 1
# example input/output:
# in: [1,2,3,4], 2
# out: 2
def find_the_kth(lst, k):
	return lst[k-1]

# find the number
# Find the number of elements of a list
# example input/output:
# in: [123, 1234, 12]
# out: 3
def find_the_number(lst):
	return len(lst)

# reverse
# Reverse a list/string
# example input/output:
# in: 'A man, a plan, a canal, panama!'
# out: '!amanap ,lanac a ,nalp a ,nam A'
def reverse(lst):
	origin_type = type(lst)
	lst = list(lst)
	lst.reverse()
	return origin_type(lst)

# check palindrome
# Find out whether a list is a palindrome. A palindrome can be read forward or backward
# example input/output:
# in: 'madamimadam'
# out: true
def check_palindrome(lst):
	lst = list(lst)
	r_lst = lst[:]
	r_lst.reverse()
	return r_lst == lst

# flatten
# Flatten a nested list structure. Transform a list, possibly holding lists as elements into a `flat' list by replacing each list with its elements (recursively).
# example input/output:
# in: [a,[b,[c,d],e]]
# out: [a,b,c,d,e]
def flatten(nested):
	res = []
	for item in nested:
		if type(item) == list:
			res.extend(item)
		else:
			res.append(item)
	return res

# deduplicate
# Eliminate consecutive duplicates of list elements. If a list contains repeated elements they should be replaced with a single copy of the element. The order of the elements should not be changed.
# example input/output:
# in: [a,a,a,a,b,c,c,a,a,d,e,e,e,e]
# out: [a,b,c,a,d,e]
def deduplicate(lst):
	if lst == []: return []
	else:
		return lst[0:1]+[j for i, j in zip(lst, lst[1:]) if i != j]

# pack dupilicates
# Pack consecutive duplicates of list elements into sublists. If a list contains repeated elements they should be placed in separate sublists
# example input/output:
# in: [a,a,a,a,b,c,c,a,a,d,e,e,e,e]
# out: [[a,a,a,a],[b],[c,c],[a,a],[d],[e,e,e,e]]
def pack_dupilicates(lst):
	if lst == []: return []
	else:
		res = [[lst[0]]]
		last = lst[0]
		for i in lst:
			if i == last[0]:
				last.append(i)
			else:
				last = [i]
				res.append(last)
		return res

# count dupilicates
# Run-length encoding of a list. Use the result of problem P09 to implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as lists (N E) where N is the number of duplicates of the element E.
# example input/output:
# in: [a,a,a,a,b,c,c,a,a,d,e,e,e,e]
# out: [(4,a),(1,b),(2,c),(2,a),(1,d),(4,e)]
def count_dupilicates(lst):
	return [(len(i), i[0]) for i in pack_dupilicates(lst)]

