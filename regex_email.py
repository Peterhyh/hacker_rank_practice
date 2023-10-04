import re


pattern = r'^<\w+@[a-z]{1,}\.([a-z]{1,3})>$'

email = '<dexter@hotmail.com>'



print(bool(re.match(pattern, email)))
        
    


