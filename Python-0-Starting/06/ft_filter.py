def ft_filter(filter_func, iterable):
	if filter_func == None:
		new_list = [item for item in iterable if item]
		for item in new_list:
			yield item
	else:
		new_list = [item for item in iterable if filter_func(item) == True]
		for item in new_list:
			yield item


# def is_even(n):
#     return n % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

# filtered_numbers = filter(is_even, numbers)
# my_filtered_numbers = ft_filter(is_even, numbers)
# none_filtered_numbers = filter(None, numbers)
# none_my_filtered_numbers = ft_filter(None, numbers)
# print(filtered_numbers)
# for item in filtered_numbers:
#     print(item)
# print(my_filtered_numbers)
# for items in my_filtered_numbers:
#     print(items)
# print("----------------------------")
# print(none_filtered_numbers)
# for item in none_filtered_numbers:
#     print(item)
# print(none_my_filtered_numbers)
# for items in none_my_filtered_numbers:
#     print(items)