inp_str = "my name is abcd"
out_str = "MY NamE IS AbcD"

s = inp_str
str_s = s.split()
res = ""
for word in str_s:
    if len(str_s) == 0:
        new_word = word.capitalize()
        
    else:
        new_word = word[0].upper() + word[1:-1].lower() + word[-1].upper()
    res += new_word + " "

print(res)
