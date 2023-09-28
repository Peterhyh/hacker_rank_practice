
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(sorted(set(string[i:i+k]), key = string[i:i+k].index)))


string, k = 'AABCAAADA', 3
merge_the_tools(string, k)