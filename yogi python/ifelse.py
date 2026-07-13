name=input("enter Your name:")
mark=int(input("enter your mark:"))
print("\n StudentName:",name)
print("Mark:",mark)
if mark>=90:
    print("grade A")
elif mark>=75:
    print("grade B")
elif mark>=50:
    print("grade C")
    print("result:pass")
else:
    print("result:fail")
