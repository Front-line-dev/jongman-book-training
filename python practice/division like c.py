# C language division drops under zero when computing integers

# for division
normally = 7//3 # 2
print(normally)
# if the number is negative
negative = int(-7/3) # -2
negative2 = int(7/-3) # -2
negative3 = int(-7/-3) # 2
print(negative, negative2, negative3)