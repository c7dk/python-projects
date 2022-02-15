# 1. write a file
with open('hello.txt', 'w') as f:
    f.write("Hello World/n")
    f.write("This is the new text file/n")
    f.write("I feel good/n")

# ----------
# 2. read a file

with open('hello.txt', 'r') as f:
    print(f.read())