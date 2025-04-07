#task3
num=5
result=1;
if num<0:
    print("invalid number ")
elif(num==0):
    print("the factorial is 1")
else:
    for i in range(1,num+1):
        result=result*i
    print("The factorial of",num,"is",result);
