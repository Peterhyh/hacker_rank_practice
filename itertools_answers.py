#PART 1: print all the combinations possible with the given string and max number of characters
# from itertools import combinations

# test_string = 'HACK 2'
# string_maxnum = test_string.split(' ')
# string = string_maxnum[0]
# max_num = string_maxnum[1]
# for i in range(1, (int(max_num) + 1)):
#     for combo in combinations(sorted(string), i):
#         print(''.join(combo))
#-------------------------------------------------------------------------------------------------------------------------------------------

# #PART 2 print all the 2 character combinations (including duplicates)
# from itertools import combinations_with_replacement

# test_string = 'HACK 2'
# string_maxnum = test_string.split()
# string = string_maxnum[0]
# char_length = string_maxnum[1]

# for combo in combinations_with_replacement(sorted(string), int(char_length)):
#     print(''.join(combo))
#-------------------------------------------------------------------------------------------------------------------------------------------

#PART 3 Using groupby()
# from itertools import groupby

# test_integer = '1222311'

# array = ''

# for number, count in groupby(test_integer):
#     array += (f'({len(list(count))}, {number}) ')
# print(array)
#-------------------------------------------------------------------------------------------------------------------------------------------

#PART 4 find out the probability of one 'a' in all possible combinations

# from itertools import combinations

# list_length = 4
# string = 'a a c d'

# letters = string.split()

# selected_index = 2

# combination_list = list(combinations(letters, selected_index))

# count = 0

# for i in combination_list:
#     if 'a' in i:
#         count += 1

# print(count/len(combination_list))
#-------------------------------------------------------------------------------------------------------------------------------------------

#PART 5 Maximize it!
# from itertools import product

# line = '3 1000'
# arrays = ['2 5 4', '3 7 8 9', '5 5 7 8 9 10']

# K = int(line.split()[0])

# M = int(line.split()[1])

# N = []

# for i in range(int(K)):
#     array = arrays[i].split()
#     array = [int(n) for n in array]
#     array = array[1:]
# #     N.append(array)
    
# # product_values = list(product(*N))

# # maxi = 0
# for j in product_values:
#     sum = 0
#     for k in j:
#         sum += k**2
#     modu = sum % M
#     if modu > maxi:
#         maxi = modu
# print(maxi)
#-------------------------------------------------------------------------------------------------------------------------------------------