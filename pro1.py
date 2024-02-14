dic={}
name=input("enter your name ")
salary=input("enter your salary ")
while(name!="no" and salary!="no"):
    dic[name]=salary
    name=input("enter your name ")
    if(name != "no"):
       salary=input("enter your salary ")
print("this is the dictionary" , dic)
