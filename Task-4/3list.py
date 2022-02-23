x=[["Roll No.","Student Name","Marks"]]
num=int(input("Enter the no. of students:"))
for i in range(num):
    Rno=int(input("Enter Roll No:"))
    SName=input("Enter Students Name:")
    mark=float(input("Enter marks:"))
    x.append([Rno,SName,mark])
for i in range(len(x)):
    for j in range (len(x[i])):
        k=x[i][j]
        print(k,end='\t')
    print('\n')
#2nd subdivision
print("Second row of the list")
for i in x[2]:
    print(i,end='\t')
