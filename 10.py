str=input("Enter the string:")
list=[]
rev_list=[]
for i in str:
    list.append(i)

rev_list=list.copy()
rev_list.reverse()

print(rev_list)
if(list==rev_list):
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")


