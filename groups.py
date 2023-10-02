import re

string = '1234567890221'

match = re.match(r'.*(\d)(?=.*\1)', string)

if match:
    print(match.group(1))
else:
    print(-1)