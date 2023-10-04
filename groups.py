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











# import re

# string = 'aaadaa'
# combo = 'aa'
# expression = r'(?=('+ combo +'))'
# matches = re.finditer(expression, string)

# anymatch=False

# for match in matches:
#     anymatch = True
#     print((match.start(1), match.end(1)-1))


# if matches == False:
#     print((-1,-1))



import re

lines = 11
text = "a = 1;\nb = input();\n\nif a + b > 0 && a - b < 0:\nstart()\nelif a*b > 10 || a/b < 1:\nstop()\nprint set(list(a)) | set(list(b)) \nNote do not change &&& or ||| or & or |\nOnly change those '&&' which have space on both sides.\nOnly change those '|| which have space on both sides.)"


def change(number):
    if number.group(1) == '&&':
        return 'and'
    else:
        return 'or'

pattern = r'(?<= )(\|\||&&)(?= )'
print(re.sub(pattern, change, text ))