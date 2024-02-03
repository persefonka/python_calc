def calc(x,y,choice):
    if choice == '+':
        return  x + y
    elif choice == '-':
        return x - y
    elif choice == '*':
        return x * y
    elif choice == '/':
        if y != 0:
            return x / y
        else:
            return "На ноль делить нельзя"
    else:
        ValueError("Ошибка: деление на ноль")

def inp_num(x,y,c):
    num1=float(x)
    num2 =float(y)
    choice=c
    return num1, num2, choice
def start():
    choice = input("Введите тип операции (+ - * /): ")
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    x,y,c=inp_num(num1,num2,choice)
    print(num1,c,num2,"=",calc(x,y,c))
#start()