str=input("Enter the string :")
uc_count=0
lc_count=0
d_count=0
sc_count=0
for i in str:
    if i.isupper():
        uc_count+=1
    elif i.islower():
        lc_count+=1
    elif i.isdigit():
        d_count+=1
    else:
        sc_count+=1

print("Digits Count:",d_count)
print("Upper Case Count:",uc_count)
print("Lower Case Count:",lc_count)
print("Special Characters Count:",sc_count)
      
        
        
