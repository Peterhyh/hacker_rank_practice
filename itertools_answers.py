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