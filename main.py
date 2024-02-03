def inputt():
    num1=int(input())
    num2=int(input())
    choice=input()
    return num1, num2, choice
def calc(num1, num2, choice):
    if choice=="+":
        return num1+num2
    elif choice=="-":
        return num1-num2
    else:
        return 0
def start():
    x,y,z=inputt()
    print(calc(x,y,z))
start()


