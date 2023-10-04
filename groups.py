# import re

# string = '1234567890'

# match = re.match(r'.*(\d)(?=.*\1)', string)

# if match:
#     print(match.group(1))
# else:
#     print(-1)



# import re

# expression=r'(?<=[^aeiouAEIOU0-9+-])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU0-9+-])'

# string='rabcdeefgyYhFjkIoomnpOeorteeeeet'

# matches = re.findall(expression, string)


# if matches:
#     for match in matches:
#         print(match)
# else:
#     print(-1)

import re

string = 'aaadaa'
combo = 'aa'
expression = r'(?=('+ combo +'))'
matches = re.finditer(expression, string)




anymatch=False

for match in matches:
    anymatch = True
    print((match.start(1), match.end(1)-1))


if matches == False:
    print((-1,-1))

