import re

x = 'B1cD102354'

uppercase_pattern = r'[A-Z]'
number_pattern = r'[0-9]'
alphanumeric_pattern = r'^[a-zA-Z0-9]*$'
max_count_pattern = r'{10}'

class IdCheck():
    def uppercase(self, id):
        upper_count = len(re.findall(uppercase_pattern, id))
        if upper_count >= 2:
            return True
        else:
            return False

    def number(self, id):
        number_count = len(re.findall(number_pattern, id))
        if number_count >= 3:
            return True
        else:
            return False

        
    def validity(self, id):
        alphanumeric = bool(re.match(alphanumeric_pattern, id))
        count = bool(re.match(max_count_pattern, id))
        
        id_char = set()
        for char in id_char:
            if char in id_char:
                valid_char = False
            id_char.add(char)

        if alphanumeric == True and count == True and valid_char == True:
            return True
        else:
            return False
        

check = IdCheck()




