
def minion_game(string):
    Vowels = ['A', 'E', 'I', 'O', 'U']

    Kevin_score = 0
    Stuart_score = 0


    for i in range(len(string)):
        if string[i] in Vowels:
            Kevin_score += (len(string)-i)
        else:
            Stuart_score += (len(string)-i)


    if Kevin_score > Stuart_score:
        print("Kevin", Kevin_score)
    elif Stuart_score > Kevin_score:
        print("Stuart", Stuart_score)
    else:
        print("Draw")

        


s = 'BANANA'
minion_game(s)