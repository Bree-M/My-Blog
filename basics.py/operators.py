#language of logic, how it makes decisions and do the math.
#Operators are how Python understands intent. It's not enough to have values — we have to know how they relate, act, and feel about each other.
#(+	Addition	2 + 3 → 5
# -	Subtraction	5 - 2 → 3
# *	Multiplication	4 * 2 → 8
# /	Division	8 / 2 → 4.0
# //	Floor Division	9 // 2 → 4
# %	Modulus	9 % 2 → 1 (gives remainder)
# **	Exponentiation	2 ** 3 → 8
# ==	Equal?	5 == 5 → True
# !=	Not equal?	5 != 3 → True
# >	Greater than?	7 > 5 → True
# <	Less than?	3 < 9 → True
# >=	Greater or equal?	6 >= 6 → True
# <=	Less or equal?	4 <= 4 → True
# and	Both must be True	True and True → True
# or	Either can be True	True or False → True
# not	Flips the truth	not True → False

age = 24
has_ID = True

can_enter_club = age >=18 and has_ID
print("Can enter club:", can_enter_club)



