import re

lines = 6

array = ['4123456789123456', '5123-4567-8912-3456', '61234-567-8912-3456', '4123356789123456', '5133-3367-8912-3456', '5123 - 3567 - 8912 - 3456']



for i in range(lines):
    card_num = array[i]
    if bool(re.match(r'^[456]', card_num)): #check if string starts with 4,5, or 6
            if bool(re.match(r'^(-?\d{4}){4}$', card_num)): #check if there are 4 sets of 4 digits that starts with a '-' or not
                digits = re.findall(r'\d', card_num)
                result = ''.join(digits)
                if bool(re.search(r'(.)\1{3,}', result)) == False: #check to see if the digits repeats 4 or more times
                     print('Valid')
                else:
                     print('Invalid')
                     
            else:
                 print('Invalid')
    else:
        print('Invalid')


# expected output:
# Valid
# Valid
# Invalid
# Valid
# Invalid
# Invalid