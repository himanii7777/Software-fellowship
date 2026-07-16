#f=open("student.txt","w")
#f.write

#read operations
#f=open("student.txt","r")
#lines=f.readlines()
#val=f.read(7)
#print (lines)
#print(val)

with open('student.txt','r') as file:
    char=file.read(10)
    current_pos =file.tell()
    file.seek(15)
    print(char)
    print(current_pos)

    names-[]
    age=[]
    n=input("Enter name")
    a=input("Enter age")
    names.append(n)
    age.append(a)

    with open('student.txt','w') as f:
        for i in range (len(names)):
f.write
