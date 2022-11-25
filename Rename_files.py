#!/usr/bin/env python3
import os
first=int(input("Enter first number: "))
last=int(input("Enter last number: "))
ext=input("Enter file extension: ")
c=1
for i in range(first,last+1):
    if os.path.exists("IMG_"+str(i)+"."+ext):
       with open("IMG_"+str(i)+"."+ext) as file:
          os.rename(file,"Gender Reveal "+str(c)+"."+ext)
          c+=1
print("Number of files renamed : "+str(c))
