#!/usr/bin/env python3
import os
first=int(input("Enter first number: "))
last=int(input("Enter last number: "))
ext=input("Enter file extension: ")
new_name=input("Enter new name: ")
c=1
for i in range(first,last+1):
    file_name="IMG_"+str(i)+"."+ext
    if os.path.exists(file_name):
          os.rename(file_name,new_name+" "+str(c)+"."+ext)
          c+=1
print("Number of files renamed : "+str(c))
