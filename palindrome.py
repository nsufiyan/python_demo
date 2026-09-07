def isPalindrome(str1):
    i=0
    j=len(str1)-1

    while i<=j:
        if str1[i]==str1[j]:
           i=i+1
           j=j-1
        else:
           return False
    return True

str1=input("enter the string:")
print(isPalindrome(str1))
