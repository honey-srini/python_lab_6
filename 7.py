str=input("Enter the string:")
count=0
for i in str:
    for j in str:
        if i==j:
            count+=1
    print(i,":",count)
    count=0


