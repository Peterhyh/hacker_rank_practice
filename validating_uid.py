import re

x = 'B1CD102354'

uppercase_pattern = r'[A-Z]'


class IdCheck():
    def check_upper(self, id):
        upper_count = len(re.findall(uppercase_pattern, id))
        if upper_count >= 2:
            return True




check = IdCheck()


print(check.check_upper(x))