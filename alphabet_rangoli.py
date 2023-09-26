# #size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10
# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------


import string

# abcdefghijklmnopqrstuvwxyz


def print_rangoli(size):
    width = 4 * size - 3 #setting the width needed to fit the pattern
    alpha = string.ascii_lowercase #generating all the letters of the alphabet as a string
    for i in list(range(size))[::-1] + list(range(1, size)): #looping through all the numbers from 0 to 9in reverse (9,8,7,6,5,4,3,2,1,0) and then increment of 1 after reaching 0 (1,2,3,4,5,6,7,8,9).
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))




n = 10
print_rangoli(n)