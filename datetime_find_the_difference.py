
from datetime import datetime

def time_delta(t1, t2):
    format_ = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, format_)
    t2= datetime.strptime(t2, format_)
    
    return(str(int(abs((t1-t2).total_seconds()))))
    
t = 2

t1_arr = ['Sun 10 May 2015 13:54:36 -0700', 'Sat 02 May 2015 19:54:36 +0530']
t2_arr = ['Sun 10 May 2015 13:54:36 -0000', 'Fri 01 May 2015 13:54:36 -0000']

for i in range(t):
    t1 = t1_arr[i]

    t2 = t2_arr[i]
    
    delta = time_delta(t1, t2)

    print(delta)



