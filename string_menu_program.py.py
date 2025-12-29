#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Menu-driven string operations program
# Covers length, case conversion, palindrome check, etc.
# Written as part of Python practice
value=""
while True:
    print("\n.......MENU......")
    print("0. ENTER A STRING")
    print("1. LENGTH OF STRING")
    print("2. UPPERCASE")
    print("3. LOWERCASE")
    print("4. REVERSE A STRING")
    print("5. CHECK IF IT IS PALLINDROME")
    print("6. COUNT A CHARACTER ")
    print("7. REPLACE A CHARACTER")
    print("8. STRING CONCATENATION")
    print("9. EXIT")
    try:
        choice=int(input("CHOOSE AN OPERATION FROM 0-9: "))
    except ValueError:
        print("ENTER ONLY NUMBERS")
        continue
    if choice==0:
         value=input("ENTER A STRING")
         print("ENTERED STRING IS : ",value)
    elif choice==1:
        if value=="":
            print("ENTER STRING FIRST USING OPTION '0' FROM THE MENU")
        else:
            print("THE LENGTH IS:",len(value))
    elif choice==2:
        print("THE UPPERCASE: ",value.upper())
    elif choice==3:
        print("THE LOWERCASE: ",value.lower())
    elif choice==4:
        print("THE REVERSED STRING: ",value[::-1])
    elif choice==5:
        if value==value[::-1]:
            print("YES IT IS PALINDROME")
        else:
            print("NOT A PALINDROME")
    elif choice==6:
        char=input("ENTER A CHARACTER")[0]
        print("THE COUNT OF ",char," IS",value.count(char))
    elif choice==7:
        oldchar=input("ENTER A CHARACTER TO BE REPLACED")
        newchar=input("ENTER NEW CHARACTER")
        if oldchar in value:
            print("THE REPLACED STRING: ",value.replace(oldchar,newchar))
        else:
            print("NOT PRESENT IN STRING")
    elif choice==8:
        newstr=input("ENTER NEW STRING")
        print("THE NEW STRING IS : ",value + " " + newstr)
    elif choice==9:
        print("EXITING.....")
        break
    else:
        print("PLEASE CHOOSE THE NUMBERS BETWEEN 0-9")




# In[ ]:




