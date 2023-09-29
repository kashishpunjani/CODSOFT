
#................... Password Generator .........................
import string,secrets,random,array
#new..........................
MAX_lEN = int(input('enter the desired length of the password : '))
no = string.digits
upp = string.ascii_uppercase
low = string.ascii_lowercase
sym = string.punctuation
total = no + upp + low + sym
# by using combination we get 26 lower + 26 uper + 10 digit + 32 symbol = 94 length


#1 leter from each = 4
rand_upper = random.choice(upp)
rand_lower = random.choice(low)
rand_digit = random.choice(no)
rand_symbol = random.choice(sym)

# 4 character
temp = rand_upper+ rand_lower +rand_digit +rand_symbol

#total = 94 , temp = 4  maxlenght = 12

for x in range(MAX_lEN - 4):             # 12 - 4 = 7
    temp = temp + random.choice(total)   # temp = 4 # total = 94 but due to random it take 1 no. ---->temp = 4+1  => 5
    temp_pass_list = array.array('u', temp)  # u is use for unicode character here temp_pass_list gives random 12 character
    random.shuffle(temp_pass_list) # range of x is 7
password = ''
for x in temp_pass_list:
    password = password+ x

print(password)

