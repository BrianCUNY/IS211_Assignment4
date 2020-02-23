#! /usr/bin/env python3

#IS211 Assignment 4, 2/2

import time
import random

def insertion_sort(a_list):
	#sorts a list by insertion sort and returns processing time
	start_time = time.time()
	for index in range(1, len(a_list)):
		current_value = a_list[index]
		position = index
		while position > 0 and a_list[position - 1] > current_value:
			a_list[position] = a_list[position - 1]
			position = position - 1
		a_list[position] = current_value
	end_time = time.time()
	run_time = end_time - start_time
	return(run_time, a_list)

def gap_insertion_sort(a_list, start, gap):
	#sorts a list by gap insertion
	for x in range(start + gap, len(a_list), gap):
		current_value = a_list[x]
		position = x
		while position >= gap and a_list[position - gap] > current_value:
			a_list[position] = a_list[position - gap]
			position = position - gap
		a_list[position] = current_value
		
def shell_sort(a_list):
	#sorts a list by shell sort
	start_time = time.time()
	sublist_count = len(a_list) // 2
	while sublist_count > 0:
		for start_position in range(sublist_count):
			gap_insertion_sort(a_list, start_position, sublist_count)
		sublist_count = sublist_count // 2
	end_time = time.time()
	run_time = end_time - start_time
	return(run_time, a_list)
	
def python_sort(a_list):
	#sorts a list using pythons built in sort
	start_time = time.time()
	a_list.sort()
	end_time = time.time()
	run_time = end_time - start_time
	return(run_time, a_list)
	
def generated_list(max_value):
	#creates a generated list of random values
	sample_list = random.sample(range(1, (max_value + 1)), max_value)
	return sample_list

def main():
	#tests the above sort algorithms, creates 100 test lists in 500,1000,10000 size and calculates processing time
	sample_size = [500, 1000, 10000]
	tests = {'Insertion': 0, 'Shell': 0, 'Python': 0}
	for sample in sample_size:
		counter = 0
		while counter < 100:
			test_list = generated_list(sample)
			tests['Insertion'] += insertion_sort(test_list)[0]
			tests['Shell'] += shell_sort(test_list)[0]
			tests['Python'] += python_sort(test_list)[0]
			counter += 1
		print('for sample size %s:' % (sample))
		for test in tests:
			print('%s Sort took %10.7f seconds to run, ' 'on average.' % (test, tests[test] / counter))
			
if __name__ == '__main__':
	main()
