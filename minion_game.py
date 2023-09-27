def filter(letters):
    result = []

    for j in range(0, len(letters)):
        if letters[j] in result:
            continue
        else:
            result.append(letters[j])
    return(result)

def minion_game(string):
    vowels_points = 0
    consonants_points = 0
    
    vowels = ['A', 'E', 'I', 'O', 'U',]

    string_vowels = []
    string_consonants = []
    
    for i in string:
        if i in vowels:
            string_vowels.append(i)
        else:
            string_consonants.append(i)


    filtered_vowels = filter(string_vowels)
    filtered_consonants = filter(string_consonants)

    final_consonants = []

    start_index = string.index(filtered_consonants[0])
    new_string = string[start_index:]

    for i in range(0, len(new_string)):
        final_consonants.append(new_string[i])
                

    for i in range(0, len(final_consonants)):
        final_consonants[i]
    
        


s = 'BANANA'
minion_game(s)