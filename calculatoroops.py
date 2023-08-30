class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

k=Calculator()
while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    l=int(input("Select operation from above:"))
    if l in(1,2,3,4,5):
        if(l==5):
            print("Invalid input")
            break
        a=int(input("Enter 1st number:"))
        b=int(input("Enter 2nd number"))

        if(l==1):
            print(a,"+",b,"=",k.add(a,b))
        elif(l==2):
            print(a,"-",b,"=",k.subtract(a,b))
        elif(l==3):
            print(a,"*",b,"=",k.multiply(a,b))
        elif(l==4):
            print(a,"/",b,"=",k.divide(a,b))
