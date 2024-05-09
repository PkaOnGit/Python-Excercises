def count(x):
    char = sum(1 for i in x if i.isalpha())
    digit = sum(1 for i in x if i.isdigit())
    other = len(x) - char - digit
    return char, digit, other


        


x = input("File here")
y = input("write file")
with open(x,'r') as file:
    text = file.read()
    print(text)
    char, digit, other = count(x)


with open(y,'w') as write_file:
    write_file.write("me")
    write_file.write(f"{char}\n")
    write_file.write(f"{digit}\n")
    write_file.write(f"{other}\n")