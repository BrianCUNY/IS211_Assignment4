#! /usr/bin/env python3

#IS211 Assignment 4, 1/2

import time
import random

def sequential_search(a_list, item):
	#searches a list in sequential order and returns a T/F if present along with processing time
	start_time = time.time()
	pos = 0
	found = False
	while pos < len(a_list) and not found:
		if a_list[pos] == item:
			found = True
		else:
			pos = pos + 1
	end_time = time.time()
	run_time = end_time - start_time
	return(run_time, found)

def ordered_sequential_search(a_list, item):
	#searches a ordered list in sequential order and returns a T/F if present along with processing time
	a_list = sorted(a_list)
	start_time = time.time()
	pos = 0
	found = False
	stop = False
	while pos < len(a_list) and not found and not stop:
		if a_list[pos] == item:
			stop = True
		else:
			pos = pos + 1
	end_time = time.time()
	run_time = end_time - start_time
	return(run_time, found)

def binary_search_iterative(a_list, item):
	#searches a ordered list for a given value and returns a T/F if present along with processing time
	a_list = sorted(a_list)
	start_time = time.time()
	first = 0
	last = len(a_list) - 1
	found = False
	while first <= last and not found:
		midpoint = (first + last) // 2
		if a_list[midpoint] == item:
			found = True
		else:
			if item < a_list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	end_time = time.time()
	run_time = end_time - start_time
	return(run_time, found)

def binary_search_recursive(a_list_, item):
	#searches a ordered list for a given value and returns a T/F if present along with processing time
	a_list = sorted(a_list)
	start_time = time.time()
	if len(a_list) == 0:
		found = False
	else:
		midpoint = len(a_list) // 2
		if a_list[midpoint] == item:
			found = True
		else:
			if item < a_list[midpoint]:
				return binary_search_recursive(a_list[:midpoint], item)
			else:
				return binary_search_recursive(a_list[midpoint + 1:], item)
	end_time = time.time()
	run_time = end_time - start_time
	return(run_time, found)

def generated_list(max_value):
	#creates a generated list of random values
	sample_list = random.sample(range(1, (max_value + 1)), max_value)
	return sample_list

def main():
	#tests the above search algorithms, creates 100 test lists in 500,1000,10000 size and calculates processing time
	sample_size = [500, 1000, 10000]
	tests = {'Sequential': 0, 'Ordered': 0, 'Binary Iterative': 0, 'Binary Recursive': 0}
	for sample in sample_size:
		counter = 0
		while counter < 100:
			test_list = generated_list(sample)
			tests['Sequential'] += sequential_search(test_list, -1)[0]
			tests['Ordered'] += ordered_sequential_search(test_list, -1)[0]
			tests['Binary Iterative'] += binary_search_iterative(test_list, -1)[0]
			tests['Binary Recursive'] += binary_search_recursive(test_list, -1)[0]
			counter += 1
		print('For sample size %s:' % (sample))
		for test in tests:
			print('%s Search took %107f seconds to run, ' 'on average.' % (test, tests[test] / counter))
			
if __name__ == "__main__":
	main()
