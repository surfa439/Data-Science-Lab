st1=input("Enter First List:\n")
list1=st1.split()
st2=input("Enter Second List:\n")
list2=st2.split()
print(list1)
print(list2)
flag=0
for i in list1:
    for j in list2:
        if i==j:
            flag=1
if flag==1:
    print("True")
else:
    print("False")
