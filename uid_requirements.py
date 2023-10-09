# A valid UID must follow the rules below:
# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0-9).
# It should only contain alphanumeric characters (a-z,A-Z & 0-9).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.


import re

num_tests = 2

id_array =['B1cD102354','B1TDF02354']

for i in range(num_tests):
    id = id_array[i]
    if id.isalnum() and len(id) == 10:
        if re.search(r'(.*[A-Z]){2,}', id) and re.search(r'(.*[0-9]){3,}', id):
            if re.search(r'.*(.).*\1+', id):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')

