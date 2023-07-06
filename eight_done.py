import pickle

with open("test1.txt", 'r') as f:
    lines = f.readlines()

with open("test2.txt", 'w') as f2:
    for line in lines:
        f2.write(line[::-1])

f3 = open('test2.txt', 'r')
f4 = open('test1.txt', 'r')
print(f4.read())
print(f3.read())