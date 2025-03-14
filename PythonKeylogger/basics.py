# storing the keystrokes in a text file
# File Handling - How to read, write and append the file

#write a file
f = open("log.txt",'w')
f.write("i am awesome")
f.close()


#read a file
f = open("log.txt",'r')
filedata = f.read()
print(filedata)
#f.write("i am awesome")
f.close()


#append a file
f = open("log.txt",'a')
f.write("i awesome my g")
f.close()


#with releases resources automatically(no need to close)
with open("log.txt",'a') as f:
    f.write("my guy")