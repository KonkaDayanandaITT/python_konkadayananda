input_file = open("sample.txt", "r")
text = input_file.read()
input_file.close()

words = text.split()

new_txt = ""
for word in words:
    new_txt = new_txt + word.capitalize() + " "

new_txt = new_txt.strip()

count = new_txt.count(" ")

output_file = open("output.txt", "w")
output_file.write(new_txt.strip())
output_file.close()

print("The white spaces present in text is:", count)
