n=input("enter a string:")
s1=set('aeiouAEIOU')
count=0
for i in n:
    if i in s1:
        count+=1
print("the vowel count in the given string is ",count)
    
