f=open("test.txt")
filelines=f.readlines()
for line in filelines:
    print(line)

intro="My name is Pulkit,i am 14 years old"
words=intro.split(",")
print(words)

def greet(name):
    print("Hello "+name+" How are you?")

greet("Diksha")