file = open("sample.txt",'r')
text = file.read()
file.close()

words = text.split()

new_txt = ""
for w in words:
    new_txt = new_txt+ w.capitalize()+" "

new_txt = new_txt.strip()
count = new_txt.count(" ")

count = 0

for i in new_txt:
    if i == " ":
        count = count + 1

final = open("sample.txt",'w')
final.write(new_txt.strip())
final.close()

print("The white spaces present in text is:",count)